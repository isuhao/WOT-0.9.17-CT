# 2016.11.19 19:50:53 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/server_events/events_helpers.py
import operator
import time
import types
from collections import namedtuple, defaultdict
from functools import partial
import BigWorld
import constants
from adisp import async
from constants import EVENT_TYPE
from debug_utils import LOG_ERROR
from gui import GUI_SETTINGS
from gui import makeHtmlString
from gui.LobbyContext import g_lobbyContext
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.server_events import formatters, conditions, settings as quest_settings, caches
from gui.server_events.bonuses import getTutorialBonusObj
from gui.server_events.event_items import DEFAULTS_GROUPS
from gui.server_events.modifiers import ACTION_MODIFIER_TYPE
from gui.shared import g_itemsCache
from gui.shared.formatters import text_styles
from gui.shared.gui_items import Vehicle
from gui.shared.gui_items.processors import quests as quests_proc
from gui.shared.utils.decorators import process
from gui.shared.utils.requesters.ItemsRequester import FALLOUT_QUESTS_CRITERIA
from helpers import i18n, int2roman, time_utils, dependency
from potapov_quests import PQ_BRANCH
from quest_xml_source import MAX_BONUS_LIMIT
from shared_utils import CONST_CONTAINER
from skeletons.gui.server_events import IEventsCache
_AWARDS_PER_PAGE = 3
FINISH_TIME_LEFT_TO_SHOW = time_utils.ONE_DAY
START_TIME_LIMIT = 5 * time_utils.ONE_DAY
RENDER_BACKS = {1: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_QUESTS_BACK_EXP,
 2: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_QUESTS_BACK_ITEMS,
 3: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_QUESTS_BACK_PREMDAYS,
 4: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_QUESTS_BACK_VEHICLES,
 1000: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_HISTORICAL_ANY,
 1001: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_HISTORICAL_WITH_BATTLES,
 2000: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_PERIODIC_DAILY,
 2001: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_PERIODIC_WEEKLY,
 3000: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_HOLIDAYS_WG_BIRTHDAY,
 4000: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_NEW_YEAR_0,
 4001: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_NEW_YEAR_1,
 4002: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_NEW_YEAR_2,
 4003: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_NEW_YEAR_RU_0,
 4004: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_NEW_YEAR_RU_1,
 4005: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_NEW_YEAR_3,
 5000: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_RANDOM_0,
 5001: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_RANDOM_1,
 5002: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_RANDOM_2,
 5003: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_RANDOM_3,
 5004: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_RANDOM_4,
 5005: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_RANDOM_5,
 5006: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_RANDOM_6,
 DEFAULTS_GROUPS.UNGROUPED_QUESTS: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_OTHER_QUESTS,
 DEFAULTS_GROUPS.UNGROUPED_ACTIONS: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_SALES,
 DEFAULTS_GROUPS.CURRENTLY_AVAILABLE: RES_ICONS.MAPS_ICONS_QUESTS_EVENTBACKGROUNDS_CURRENTLY_AVAILABLE}

class EVENT_STATUS(CONST_CONTAINER):
    COMPLETED = 'done'
    NOT_AVAILABLE = 'notAvailable'
    NONE = ''


class _EventInfo(object):
    NO_BONUS_COUNT = -1

    def __init__(self, event):
        self.event = event

    def getInfo(self, svrEvents, pCur = None, pPrev = None, noProgressInfo = False):
        if noProgressInfo:
            status, statusMsg = EVENT_STATUS.NONE, self._getStatus()[1]
            bonusCount = self.NO_BONUS_COUNT
            qProgCur, qProgTot, qProgbarType, tooltip = (0,
             0,
             formatters.PROGRESS_BAR_TYPE.NONE,
             None)
        else:
            bonusCount = self._getBonusCount(pCur)
            status, statusMsg = self._getStatus(pCur)
            qProgCur, qProgTot, qProgbarType, tooltip = self._getProgressValues(svrEvents, pCur, pPrev)
        bgImage = RENDER_BACKS.get(self.event.getIconID(), '')
        showBgImage = len(bgImage) > 0
        isAvailable, _ = self.event.isAvailable()
        return {'questID': str(self.event.getID()),
         'eventType': self.event.getType(),
         'IGR': self.event.isIGR(),
         'taskType': self.event.getUserType(),
         'tasksCount': bonusCount,
         'progrBarType': qProgbarType,
         'progrTooltip': tooltip,
         'maxProgrVal': qProgTot,
         'currentProgrVal': qProgCur,
         'rendererType': QUESTS_ALIASES.RENDERER_TYPE_QUEST,
         'showBckgrImage': showBgImage,
         'bckgrImage': bgImage,
         'timerDescription': self._getTimerMsg(),
         'status': status,
         'description': self.event.getUserName(),
         'tooltip': TOOLTIPS.QUESTS_RENDERER_LABEL,
         'isSelectable': True,
         'isNew': quest_settings.isNewCommonEvent(self.event),
         'isAvailable': isAvailable}

    def getDetails(self, svrEvents):
        eProgCur, eProgTot, eProgbarType, tooltip = self._getProgressValues(svrEvents)
        status, statusMsg = self._getStatus()
        requirements = self._getRequirements(svrEvents)
        condsDescription = self._getConditionsDescription()
        topConditions = self._getTopConditions(svrEvents)
        conds = self._getConditions(svrEvents)
        hasConditions = bool(len(condsDescription) or len(topConditions) or len(conds) > 0)
        return {'header': {'title': self.event.getUserName(),
                    'date': self._getActiveDateTimeString(),
                    'status': status,
                    'statusDescription': statusMsg,
                    'progrBarType': eProgbarType,
                    'eventType': self.event.getType(),
                    'progrTooltip': tooltip,
                    'maxProgrVal': eProgTot,
                    'currentProgrVal': eProgCur,
                    'tasksCount': self._getBonusCount(),
                    'hasConditions': hasConditions,
                    'hasRequirements': len(requirements) > 0},
         'awardsDataProvider': getCarouselAwardVO(self.event.getBonuses()),
         'taskToUnlock': self._getUnlockedTokens(),
         'requirements': {'title': '',
                          'description': '',
                          'containerElements': requirements},
         'conditions': {'title': self._getConditionsTitle(),
                        'description': condsDescription,
                        'topConditions': topConditions,
                        'containerElements': conds}}

    def getActiveDateTimeString(self):
        return self._getActiveDateTimeString()

    def getConditions(self, svrEvents):
        return self._getConditions(svrEvents)

    def getPostBattleInfo(self, svrEvents, pCur, pPrev, isProgressReset, isCompleted):
        index = 0
        progresses = []
        if not isProgressReset and not isCompleted:
            for cond in self.event.bonusCond.getConditions().items:
                if isinstance(cond, conditions._Cumulativable):
                    for groupByKey, (curProg, totalProg, diff, _) in cond.getProgressPerGroup(pCur, pPrev).iteritems():
                        label = cond.getUserString()
                        if not diff or not label:
                            continue
                        index += 1
                        progresses.append({'progrTooltip': None,
                         'progrBarType': formatters.PROGRESS_BAR_TYPE.SIMPLE,
                         'maxProgrVal': totalProg,
                         'currentProgrVal': curProg,
                         'description': '%d. %s' % (index, label),
                         'progressDiff': '+ %s' % diff})

            if not len(progresses):
                return
        alertMsg = ''
        if isProgressReset:
            alertMsg = i18n.makeString('#quests:postBattle/progressReset')
        diffStr, awards = ('', None)
        if not isProgressReset and isCompleted:
            awards = self._getBonuses(svrEvents, useIconFormat=False)
        return {'title': self.event.getUserName(),
         'awards': awards,
         'progressList': progresses,
         'alertMsg': alertMsg,
         'questInfo': self.getInfo(svrEvents, pCur, pPrev),
         'personalInfo': [],
         'questType': self.event.getType()}

    @classmethod
    def _getTillTimeString(cls, timeValue):
        if START_TIME_LIMIT >= timeValue > time_utils.ONE_DAY:
            fmt = i18n.makeString(QUESTS.ITEM_TIMER_TILLSTART_DAYS)
        elif time_utils.ONE_DAY >= timeValue > time_utils.ONE_HOUR:
            fmt = i18n.makeString(QUESTS.ITEM_TIMER_TILLSTART_HOURS)
        else:
            fmt = i18n.makeString(QUESTS.ITEM_TIMER_TILLSTART_MIN)
        gmtime = time.gmtime(timeValue)
        return fmt % {'hours': time.strftime('%H', gmtime),
         'min': time.strftime('%M', gmtime),
         'days': str(gmtime.tm_mday)}

    @classmethod
    def _getDateTimeString(cls, timeValue):
        return '{0:>s} {1:>s}'.format(BigWorld.wg_getLongDateFormat(timeValue), BigWorld.wg_getShortTimeFormat(timeValue))

    @classmethod
    def _getDailyProgressResetTimeOffset(cls):
        regionalSettings = BigWorld.player().serverSettings['regional_settings']
        if 'starting_time_of_a_new_game_day' in regionalSettings:
            newDayOffset = regionalSettings['starting_time_of_a_new_game_day']
        elif 'starting_time_of_a_new_day' in regionalSettings:
            newDayOffset = regionalSettings['starting_time_of_a_new_day']
        else:
            newDayOffset = 0
        return newDayOffset

    @classmethod
    def _getEventsByIDs(cls, ids, svrEvents):
        result = {}
        for eID in ids:
            if eID in svrEvents:
                result[eID] = svrEvents[eID]

        return result

    def _getUnlockedTokens(self):
        childQuestsNames = self.event.getParentsName()
        if len(childQuestsNames) == 1:
            questTokenName = childQuestsNames.values()[0][0]
            parentTokenName = self.event.getParents().values()[0][0]
            return {'label': formatters.formatGold(TOOLTIPS.AWARDITEM_BATTLETOKEN_ONE_BODY, name=questTokenName),
             'linkID': parentTokenName,
             'isNotAvailable': False}
        elif len(childQuestsNames) > 1:
            return {'label': formatters.formatGold(TOOLTIPS.AWARDITEM_BATTLETOKEN_DESCRIPTION),
             'linkID': None,
             'isNotAvailable': False}
        else:
            return {}

    def _getStatus(self, pCur = None):
        return (EVENT_STATUS.NONE, '')

    def _getBonusCount(self, pCur = None):
        return self.NO_BONUS_COUNT

    def _getProgressValues(self, svrEvents = None, pCur = None, pPrev = None):
        return (0,
         0,
         formatters.PROGRESS_BAR_TYPE.NONE,
         None)

    def _getBonuses(self, svrEvents, bonuses = None, useIconFormat = False):
        bonuses = bonuses or self.event.getBonuses()
        result = []
        for b in bonuses:
            if b.isShowInGUI():
                result.append(b.format())

        if len(result):
            return formatters.todict([formatters.packTextBlock(', '.join(result))])
        return []

    def _getRequirements(self, svrEvents):
        return []

    def _getConditionsTitle(self):
        return i18n.makeString('#quests:details/conditions/label')

    def _getConditionsDescription(self):
        return ''

    def _getTopConditions(self, svrEvents):
        return []

    def _getConditions(self, svrEvents):
        return []

    def _getTimerMsg(self):
        startTimeLeft = self.event.getStartTimeLeft()
        if startTimeLeft > 0:
            if startTimeLeft > START_TIME_LIMIT:
                fmt = self._getDateTimeString(self.event.getStartTime())
            else:
                fmt = self._getTillTimeString(startTimeLeft)
            return makeHtmlString('html_templates:lobby/quests', 'timerTillStart', {'time': fmt})
        if FINISH_TIME_LEFT_TO_SHOW > self.event.getFinishTimeLeft() > 0:
            gmtime = time.gmtime(self.event.getFinishTimeLeft())
            if gmtime.tm_hour > 0:
                fmt = i18n.makeString('#quests:item/timer/tillFinish/onlyHours')
            else:
                fmt = i18n.makeString('#quests:item/timer/tillFinish/lessThanHour')
            fmt %= {'hours': time.strftime('%H', gmtime),
             'min': time.strftime('%M', gmtime),
             'days': str(gmtime.tm_mday)}
            return makeHtmlString('html_templates:lobby/quests', 'timerTillFinish', {'time': fmt})
        return ''

    def _getActiveDateTimeString(self):
        i18nKey, args = None, {}
        if self.event.getFinishTimeLeft() <= time_utils.ONE_DAY:
            gmtime = time.gmtime(self.event.getFinishTimeLeft())
            if gmtime.tm_hour > 0:
                fmt = i18n.makeString(QUESTS.ITEM_TIMER_TILLFINISH_LONGFULLFORMAT)
            else:
                fmt = i18n.makeString(QUESTS.ITEM_TIMER_TILLFINISH_SHORTFULLFORMAT)
            fmt %= {'hours': time.strftime('%H', gmtime)}
            return fmt
        else:
            if self.event.getStartTimeLeft() > 0:
                i18nKey = '#quests:details/header/activeDuration'
                args = {'startTime': self._getDateTimeString(self.event.getStartTime()),
                 'finishTime': self._getDateTimeString(self.event.getFinishTime())}
            elif self.event.getFinishTimeLeft() <= time_utils.HALF_YEAR:
                i18nKey = '#quests:details/header/tillDate'
                args = {'finishTime': self._getDateTimeString(self.event.getFinishTime())}
            weekDays = self.event.getWeekDays()
            intervals = self.event.getActiveTimeIntervals()
            if len(weekDays) or len(intervals):
                if i18nKey is None:
                    i18nKey = '#quests:details/header/schedule'
                if len(weekDays):
                    days = ', '.join([ i18n.makeString('#menu:dateTime/weekDays/full/%d' % idx) for idx in self.event.getWeekDays() ])
                    i18nKey += 'Days'
                    args['days'] = days
                if len(intervals):
                    times = []
                    for low, high in intervals:
                        times.append('%s - %s' % (BigWorld.wg_getShortTimeFormat(low), BigWorld.wg_getShortTimeFormat(high)))

                    i18nKey += 'Times'
                    times = ', '.join(times)
                    args['times'] = times
            return i18n.makeString(i18nKey, **args)


class _QuestInfo(_EventInfo):
    PROGRESS_TOOLTIP_MAX_ITEMS = 4
    SIMPLE_BONUSES_MAX_ITEMS = 5

    def _getBonuses(self, svrEvents, bonuses = None, useIconFormat = False):
        bonuses = bonuses or self.event.getBonuses()
        result, simpleBonusesList, customizationsList, vehiclesList, iconBonusesList = ([],
         [],
         [],
         [],
         [])
        for b in bonuses:
            if b.isShowInGUI():
                if b.getName() == 'dossier':
                    for achieve in b.getAchievements():
                        result.append(formatters.packAchieveElementByItem(achieve))

                elif b.getName() == 'customizations':
                    customizationsList.extend(b.getList())
                elif b.getName() == 'vehicles':
                    flist = b.formattedList()
                    if flist:
                        vehiclesList.extend(flist)
                elif b.hasIconFormat() and useIconFormat:
                    iconBonusesList.extend(b.getList())
                else:
                    flist = b.formattedList()
                    if flist:
                        simpleBonusesList.extend(flist)

        if len(customizationsList):
            result.append(formatters.packCustomizations(customizationsList))
        if len(iconBonusesList):
            result.append(formatters.packIconAwardBonusBlock(iconBonusesList))
        if len(vehiclesList) > 0:
            vehiclesLbl, _ = self._joinUpToMax(vehiclesList)
            result.append(formatters.packVehiclesBonusBlock(vehiclesLbl, str(self.event.getID())))
        if len(simpleBonusesList) > 0:
            result.append(formatters.packSimpleBonusesBlock(simpleBonusesList))
        parents = [ qID for _, qIDs in self.event.getParents().iteritems() for qID in qIDs ]
        for qID, q in self._getEventsByIDs(parents, svrEvents or {}).iteritems():
            result.append(formatters.packTextBlock(i18n.makeString('#quests:bonuses/item/task', q.getUserName()), questID=qID))

        if len(result):
            return formatters.todict(result)
        return formatters.todict([formatters.packTextBlock(text_styles.alert('#quests:bonuses/notAvailable'))])

    def _getBonusCount(self, pCur = None):
        if not self.event.isCompleted(progress=pCur):
            bonusLimit = self.event.bonusCond.getBonusLimit()
            if bonusLimit is None or bonusLimit > 1 or self.event.bonusCond.getGroupByValue() is not None:
                return self.event.getBonusCount(progress=pCur)
        return self.NO_BONUS_COUNT

    def _getStatus(self, pCur = None):
        if self.event.isCompleted(progress=pCur):
            if self.event.bonusCond.isDaily():
                msg = i18n.makeString('#quests:details/status/completed/daily', time=self._getTillTimeString(time_utils.ONE_DAY - time_utils.getServerRegionalTimeCurrentDay()))
            else:
                msg = i18n.makeString('#quests:details/status/completed')
            return (EVENT_STATUS.COMPLETED, msg)
        else:
            isAvailable, errorMsg = self.event.isAvailable()
            if not isAvailable:
                timeLeftInfo = self.event.getNearestActivityTimeLeft()
                if errorMsg in ('in_future', 'invalid_weekday', 'invalid_time_interval') and timeLeftInfo is not None:
                    startTimeLeft = timeLeftInfo[0]
                    if startTimeLeft > START_TIME_LIMIT:
                        fmt = self._getDateTimeString(self.event.getStartTime())
                    else:
                        fmt = self._getTillTimeString(startTimeLeft)
                    msg = i18n.makeString('#quests:details/status/notAvailable/%s' % errorMsg, time=fmt)
                else:
                    msg = i18n.makeString('#quests:details/status/notAvailable/%s' % errorMsg)
                return (EVENT_STATUS.NOT_AVAILABLE, msg)
            bonus = self.event.bonusCond
            bonusLimit = bonus.getBonusLimit()
            if bonusLimit is None or bonusLimit >= MAX_BONUS_LIMIT:
                msg = i18n.makeString(QUESTS.DETAILS_HEADER_COMPLETION_UNLIMITED)
            else:
                groupBy = bonus.getGroupByValue()
                if bonus.isDaily():
                    key = QUESTS.DETAILS_HEADER_COMPLETION_DAILY
                    if groupBy is not None:
                        key = '#quests:details/header/completion/daily/groupBy%s' % groupBy.capitalize()
                else:
                    key = QUESTS.DETAILS_HEADER_COMPLETION_SINGLE
                    if groupBy is not None:
                        key = '#quests:details/header/completion/single/groupBy%s' % groupBy.capitalize()
                msg = i18n.makeString(key, count=bonusLimit)
            return (EVENT_STATUS.NONE, msg)

    def _getProgressValues(self, svrEvents = None, pCur = None, pPrev = None):
        current, total, progressType, tooltip = (0,
         0,
         formatters.PROGRESS_BAR_TYPE.NONE,
         None)
        groupBy = self.event.bonusCond.getGroupByValue()
        condsRoot = self.event.bonusCond.getConditions()
        if self.event.isCompleted(pCur) or condsRoot.isEmpty():
            return (current,
             total,
             progressType,
             tooltip)
        else:
            countOfCumulatives = 0
            cumulatives = defaultdict(list)
            for cond in condsRoot.items:
                if isinstance(cond, conditions._Cumulativable):
                    countOfCumulatives += 1
                    for groupByKey, (cur, tot, _, isCompleted) in cond.getProgressPerGroup(pCur, pPrev).iteritems():
                        if not isCompleted:
                            cumulatives[groupByKey].append((cur, tot))

            if groupBy is None and countOfCumulatives == 1 and len(cumulatives[None]):
                (current, total), progressType = cumulatives[None][0], formatters.PROGRESS_BAR_TYPE.SIMPLE
            else:
                avgProgressesPerGroup = []
                for groupByKey, values in cumulatives.iteritems():
                    progressesSum = sum(map(lambda (c, t): c / float(t), values))
                    avgProgressesPerGroup.append((groupByKey, int(round(100.0 * progressesSum / len(values))), 100))

                avgProgresses = sorted(avgProgressesPerGroup, key=operator.itemgetter(1), reverse=True)
                if len(avgProgresses):
                    (groupByKey, current, total), nearestProgs = avgProgresses[0], avgProgresses[1:]
                    progressType = formatters.PROGRESS_BAR_TYPE.COMMON
                    if groupBy is not None and groupByKey is not None:
                        name, names = ('', '')
                        if groupBy == 'vehicle':
                            name = g_itemsCache.items.getItemByCD(groupByKey).shortUserName
                            names = [ g_itemsCache.items.getItemByCD(intCD).shortUserName for intCD, _, __ in nearestProgs ]
                        elif groupBy == 'nation':
                            name = i18n.makeString('#menu:nations/%s' % groupByKey)
                            names = [ i18n.makeString('#menu:nations/%s' % n) for n, _, __ in nearestProgs ]
                        elif groupBy == 'class':
                            name = i18n.makeString('#menu:classes/%s' % groupByKey)
                            names = [ i18n.makeString('#menu:classes/%s' % n) for n, _, __ in nearestProgs ]
                        elif groupBy == 'level':

                            def makeLvlStr(lvl):
                                return i18n.makeString(QUESTS.TOOLTIP_PROGRESS_GROUPBY_NOTE_LEVEL, int2roman(lvl))

                            name = makeLvlStr(int(groupByKey.replace('level ', '')))
                            names = [ makeLvlStr(int(l.replace('level ', ''))) for l, _, __ in nearestProgs ]
                        note = None
                        if len(names):
                            note = makeHtmlString('html_templates:lobby/quests/tooltips/progress', 'note', {'names': ', '.join(names[:self.PROGRESS_TOOLTIP_MAX_ITEMS])})
                        tooltip = {'header': i18n.makeString(QUESTS.TOOLTIP_PROGRESS_GROUPBY_HEADER),
                         'body': makeHtmlString('html_templates:lobby/quests/tooltips/progress', 'body', {'name': name}),
                         'note': note}
            return (current,
             total,
             progressType,
             tooltip)

    def _getRequirements(self, svrEvents):
        result = []
        accReqsFmt = self.event.accountReqs.format(svrEvents, self.event)
        if accReqsFmt is not None:
            result.append(formatters.todict(accReqsFmt))
        vehReqsFmt = self.event.vehicleReqs.format(svrEvents, self.event)
        if vehReqsFmt is not None:
            result.append(formatters.todict(vehReqsFmt))
        return result

    def _getTopConditions(self, svrEvents):
        result = []
        preBattleFmt = self.event.preBattleCond.format(svrEvents, self.event)
        if preBattleFmt is not None:
            result.extend(preBattleFmt)
        descr = self.event.getDescription()
        if descr:
            result.append(formatters.packTextBlock(formatters.formatGray(descr)))
        return formatters.todict(result)

    def _getConditions(self, svrEvents):
        result = self._packConditions(svrEvents)
        return formatters.todict(result)

    def _packConditions(self, svrEvents):
        subBlocks = []
        bonus = self.event.bonusCond
        battlesLeft, battlesCount, inrow = None, None, False
        battles = bonus.getConditions().find('battles')
        if battles is not None:
            battlesCount = battles._getTotalValue()
            if not self.event.isCompleted() and bonus.getGroupByValue() is None:
                progress = battles.getProgressPerGroup()
                if None in progress:
                    curProg, totalProg, _, _ = progress[None]
                    battlesLeft = totalProg - curProg
        bonusFmtConds = bonus.format(svrEvents, event=self.event)
        if len(bonusFmtConds):
            subBlocks.extend(formatters.indexing(bonusFmtConds))
        postBattleFmtConds = self.event.postBattleCond.format(svrEvents, event=self.event)
        if len(postBattleFmtConds):
            if len(bonusFmtConds):
                subBlocks.append(formatters.packSeparator(label=i18n.makeString('#quests:details/conditions/postBattle/separator')))
            subBlocks.extend(formatters.indexing(postBattleFmtConds))
        if bonus.isDaily():
            resetHourOffset = (time_utils.ONE_DAY - self._getDailyProgressResetTimeOffset()) / 3600
            if resetHourOffset >= 0:
                subBlocks.append(formatters.packTextBlock(label=formatters.formatYellow('#quests:details/conditions/postBattle/dailyReset') % {'time': time.strftime(i18n.makeString('#quests:details/conditions/postBattle/dailyReset/timeFmt'), time_utils.getTimeStructInLocal(time_utils.getTimeTodayForUTC(hour=resetHourOffset)))}))
        result = []
        if len(subBlocks) or battlesCount:
            if not self.event.isGuiDisabled():
                result.append(formatters.packConditionsBlock(battlesCount, battlesLeft, bonus.isInRow(), conditions=subBlocks))
            else:
                result.append(formatters.packConditionsBlock(conditions=subBlocks))
        if bonus.getGroupByValue() is not None and not self.event.isGuiDisabled():
            progressesFmt = bonus.formatGroupByProgresses(svrEvents, self.event)
            if len(progressesFmt):
                result.append(formatters.packTopLevelContainer(i18n.makeString('#quests:details/conditions/groupBy/%s' % bonus.getGroupByValue()), subBlocks=progressesFmt, isResizable=len(progressesFmt) > 5))
        return result

    def _getActiveDateTimeString(self):
        timeLeft = self.event.getFinishTimeLeft()
        if timeLeft <= time_utils.THREE_QUARTER_HOUR:
            return formatters.formatYellow(QUESTS.DETAILS_HEADER_COMETOENDINMINUTES, minutes=getMinutesRoundByTime(timeLeft))
        return super(_QuestInfo, self)._getActiveDateTimeString()

    def _getTimerMsg(self):
        timeLeft = self.event.getFinishTimeLeft()
        if timeLeft <= time_utils.THREE_QUARTER_HOUR:
            return makeHtmlString('html_templates:lobby/quests', 'comeToEndInMinutes', {'minutes': getMinutesRoundByTime(timeLeft)})
        return super(_QuestInfo, self)._getTimerMsg()

    @classmethod
    def _joinUpToMax(cls, array, separator = ', '):
        if len(array) > cls.SIMPLE_BONUSES_MAX_ITEMS:
            label = separator.join(array[:cls.SIMPLE_BONUSES_MAX_ITEMS]) + '..'
            fullLabel = separator.join(array)
        else:
            label = separator.join(array)
            fullLabel = None
        return (label, fullLabel)


class _ActionInfo(_EventInfo):

    @classmethod
    def _getDateTimeString(cls, timeValue):
        return '{0:>s}'.format(BigWorld.wg_getLongDateFormat(timeValue))

    def _getConditionsTitle(self):
        return None

    def _getConditionsDescription(self):
        descr = self.event.getDescription()
        if descr:
            return formatters.formatBright(descr)
        return ''

    def _getConditions(self, svrEvents):
        modifiers = defaultdict(list)
        for m in self.event.getModifiers():
            fmtResult = m.format(self.event)
            if fmtResult is not None:
                if isinstance(fmtResult, types.DictType):
                    for fDType, fData in fmtResult.iteritems():
                        modifiers[fDType].extend(fData)

                else:
                    modifiers[m.getType()].extend(fmtResult)

        result = []
        if len(modifiers[ACTION_MODIFIER_TYPE.DISCOUNT]):
            result.append(formatters.packTopLevelContainer(i18n.makeString(QUESTS.DETAILS_MODIFIERS_TITLE_DISCOUNT), subBlocks=modifiers[ACTION_MODIFIER_TYPE.DISCOUNT]))
        availabilityModifiers = modifiers.get(ACTION_MODIFIER_TYPE.AVAILABILITY, [])
        if len(availabilityModifiers):
            result.append(formatters.packTopLevelContainer(i18n.makeString(QUESTS.DETAILS_MODIFIERS_TITLE_AVAILABILITY), subBlocks=availabilityModifiers))
        if len(modifiers[ACTION_MODIFIER_TYPE.RENT]):
            result.append(formatters.packTopLevelContainer(i18n.makeString(QUESTS.DETAILS_MODIFIERS_TITLE_DISCOUNT), subBlocks=modifiers[ACTION_MODIFIER_TYPE.RENT]))
        for fmtData in modifiers[ACTION_MODIFIER_TYPE.SELLING]:
            result.append(fmtData)

        return formatters.todict(result)

    def _getActiveDateTimeString(self):
        timeLeft = self.event.getFinishTimeLeft()
        if timeLeft <= GUI_SETTINGS.actionComeToEnd:
            return formatters.formatYellow(QUESTS.DETAILS_HEADER_COMETOEND)
        if timeLeft <= time_utils.THREE_QUARTER_HOUR:
            return formatters.formatYellow(QUESTS.DETAILS_HEADER_COMETOENDINMINUTES, minutes=getMinutesRoundByTime(timeLeft))
        return super(_ActionInfo, self)._getActiveDateTimeString()

    def _getTimerMsg(self):
        timeLeft = self.event.getFinishTimeLeft()
        if timeLeft <= GUI_SETTINGS.actionComeToEnd:
            return makeHtmlString('html_templates:lobby/quests', 'comeToEnd')
        if timeLeft <= time_utils.THREE_QUARTER_HOUR:
            return makeHtmlString('html_templates:lobby/quests', 'comeToEndInMinutes', {'minutes': getMinutesRoundByTime(timeLeft)})
        return super(_ActionInfo, self)._getTimerMsg()


class _PotapovQuestInfo(_QuestInfo):

    def _getBonuses(self, svrEvents, _ = None, useIconFormat = True):
        mainBonuses = self.event.getBonuses(isMain=True)
        addBonuses = self.event.getBonuses(isMain=False)
        return (_QuestInfo._getBonuses(self, None, bonuses=mainBonuses, useIconFormat=useIconFormat), _QuestInfo._getBonuses(self, None, bonuses=addBonuses, useIconFormat=False))

    def getPostBattleInfo(self, svrEvents, pCur, pPrev, isProgressReset, isCompleted):

        def _packCondition(titleKey, text):
            return '%s\n%s' % (text_styles.middleTitle(i18n.makeString(titleKey)), text_styles.main(text))

        def _packStatus(completed):
            if completed:
                return 'done'
            return 'notDone'

        return {'title': self.event.getUserName(),
         'questInfo': self.getInfo(svrEvents),
         'awards': None,
         'progressList': [],
         'alertMsg': '',
         'personalInfo': [{'statusStr': _packStatus(isCompleted[0]),
                           'text': _packCondition(QUESTS.QUESTTASKDETAILSVIEW_MAINCONDITIONS, self.event.getUserMainCondition())}, {'statusStr': _packStatus(isCompleted[1]),
                           'text': _packCondition(QUESTS.QUESTTASKDETAILSVIEW_ADDITIONALCONDITIONS, self.event.getUserAddCondition())}],
         'questType': self.event.getType()}


class _MotiveQuestInfo(_QuestInfo):

    def getDetails(self, svrEvents):
        infoList = []
        conditions = [formatters.todict(formatters.packQuestDetailsSeparator(0, 0, 5, 10))]
        conditions.extend(self._getTopConditions(svrEvents))
        conditions.append(formatters.todict(formatters.packQuestDetailsSeparator(0, 0, 10, 5)))
        conditions.extend(self._getConditions(svrEvents))
        conditionsContainer = formatters.todict(formatters.packMotiveContainer(title=i18n.makeString('#quests:quests/conditions'), subBlocks=conditions))
        infoList.append(conditionsContainer)
        requirementContainer = formatters.todict(formatters.packTopLevelContainer(title=i18n.makeString('#quests:quests/requirements'), subBlocks=[formatters.packTextBlock(formatters.formatGray(self.event.getRequirementsStr()))]))
        infoList.append(requirementContainer)
        infoList.append(formatters.todict(formatters.packQuestDetailsSeparator(0, 0, 5, 0)))
        tpsContainer = formatters.todict(formatters.packTopLevelContainer(title=i18n.makeString('#quests:QuestTaskDetailsView/description'), subBlocks=[formatters.packTextBlock(formatters.formatGray(self.event.getTips()))]))
        infoList.append(tpsContainer)
        return {'image': RES_ICONS.MAPS_ICONS_HANGARTUTORIAL_GOALSQUEST,
         'title': text_styles.highTitle(self.event.getUserName()),
         'infoList': infoList,
         'awards': self._getBonuses(svrEvents, useIconFormat=False)}

    def getPostBattleInfo(self, svrEvents, pCur, pPrev, isProgressReset, isCompleted):
        filterFunc = lambda quest: quest.getType() == EVENT_TYPE.MOTIVE_QUEST and not quest.isCompleted()
        motiveQuests = filter(filterFunc, svrEvents.values())
        info = super(_MotiveQuestInfo, self).getPostBattleInfo(svrEvents, pCur, pPrev, isProgressReset, isCompleted)
        info.update({'isLinkBtnVisible': len(motiveQuests) > 0})
        return info

    def _getTopConditions(self, svrEvents):
        result = []
        preBattleFmt = self.event.preBattleCond.format(svrEvents, self.event)
        if preBattleFmt is not None:
            result.extend(preBattleFmt)
        return formatters.todict(result)

    def _packConditions(self, svrEvents):
        result = super(_MotiveQuestInfo, self)._packConditions(svrEvents)
        descr = self.event.getDescription()
        if descr:
            result.append(formatters.packTextBlock(formatters.formatGray(descr)))
        return result


class _ClubsQuestInfo(_QuestInfo):

    def _getBonuses(self, svrEvents, bonuses = None, useIconFormat = False):
        return super(_QuestInfo, self)._getBonuses(svrEvents, bonuses, useIconFormat)


def getEventInfoData(event):
    if event.getType() == constants.EVENT_TYPE.POTAPOV_QUEST:
        return _PotapovQuestInfo(event)
    if event.getType() == constants.EVENT_TYPE.CLUBS_QUEST:
        return _ClubsQuestInfo(event)
    if event.getType() == constants.EVENT_TYPE.MOTIVE_QUEST:
        return _MotiveQuestInfo(event)
    if event.getType() in constants.EVENT_TYPE.QUEST_RANGE:
        return _QuestInfo(event)
    if event.getType() == constants.EVENT_TYPE.ACTION:
        return _ActionInfo(event)
    return _EventInfo(event)


def getMinutesRoundByTime(timeLeft):
    timeLeft = int(timeLeft)
    return (timeLeft / time_utils.QUARTER_HOUR + cmp(timeLeft % time_utils.QUARTER_HOUR, 0)) * time_utils.QUARTER


def getEventInfo(event, svrEvents = None, noProgressInfo = False):
    return getEventInfoData(event).getInfo(svrEvents, noProgressInfo=noProgressInfo)


def getEventActiveDateString(event):
    return getEventInfoData(event).getActiveDateTimeString()


def getEventDetails(event, svrEvents = None):
    return getEventInfoData(event).getDetails(svrEvents)


def getEventConditions(event, svrEvents = None):
    return getEventInfoData(event).getConditions(svrEvents)


def getEventPostBattleInfo(event, svrEvents = None, pCur = None, pPrev = None, isProgressReset = False, isCompleted = False):
    return getEventInfoData(event).getPostBattleInfo(svrEvents, pCur or {}, pPrev or {}, isProgressReset, isCompleted)


def getTutorialEventsDescriptor():
    try:
        from tutorial.doc_loader import getQuestsDescriptor
    except ImportError:
        LOG_ERROR('Can not load package tutorial')

        def getQuestsDescriptor():
            return None

    return getQuestsDescriptor()


def getTutorialQuestsBoosters():
    result = defaultdict(list)
    descriptor = getTutorialEventsDescriptor()
    completed = g_itemsCache.items.stats.tutorialsCompleted
    if descriptor is not None:
        for chapter in descriptor:
            if not chapter.isBonusReceived(completed) and chapter.getChapterStatus(descriptor, completed) == EVENT_STATUS.NONE:
                bonus = chapter.getBonus()
                if bonus is not None:
                    goodies = bonus.getValues().get('goodies', {})
                    boosterBonus = getTutorialBonusObj('goodies', goodies)
                    for booster, count in boosterBonus.getBoosters().iteritems():
                        if booster.enabled:
                            result[chapter].append((booster, count))

    return result


def getBoosterQuests():
    eventsCache = dependency.instance(IEventsCache)
    hasTopVehicle = len(g_itemsCache.items.getVehicles(FALLOUT_QUESTS_CRITERIA.TOP_VEHICLE))
    isFalloutQuestEnabled = g_lobbyContext.getServerSettings().isFalloutQuestEnabled()
    return eventsCache.getAllQuests(lambda q: q.isAvailable()[0] and not q.isCompleted() and len(q.getBonuses('goodies')) and not (q.getType() == EVENT_TYPE.POTAPOV_QUEST and q.getPQType().branch == PQ_BRANCH.FALLOUT and (not isFalloutQuestEnabled or not hasTopVehicle)), includePotapovQuests=True)


class _PotapovDependenciesResolver(object):
    eventsCache = dependency.descriptor(IEventsCache)
    _DEPENDENCIES_LIST = namedtuple('HandlersList', ['cache',
     'progress',
     'selectProcessor',
     'refuseProcessor',
     'rewardsProcessor',
     'sorter'])

    @classmethod
    def _makeRandomDependencies(cls):
        return cls._DEPENDENCIES_LIST(cls.eventsCache.random, cls.eventsCache.randomQuestsProgress, quests_proc.RandomQuestSelect, quests_proc.RandomQuestRefuse, quests_proc.PotapovQuestsGetRegularReward, partial(sorted, cmp=Vehicle.compareByVehTypeName))

    @classmethod
    def _makeFalloutDependencies(cls):
        return cls._DEPENDENCIES_LIST(cls.eventsCache.fallout, cls.eventsCache.falloutQuestsProgress, quests_proc.FalloutQuestSelect, quests_proc.FalloutQuestRefuse, quests_proc.PotapovQuestsGetRegularReward, sorted)

    @classmethod
    def chooseList(cls, questsType = None):
        if questsType is None:
            questsType = caches.getNavInfo().selectedPQType
        if questsType == QUESTS_ALIASES.SEASON_VIEW_TAB_RANDOM:
            depList = cls._makeRandomDependencies()
        else:
            depList = cls._makeFalloutDependencies()
        return depList


def getPotapovQuestsCache(questsType = None):
    return _PotapovDependenciesResolver.chooseList(questsType).cache


def getPotapovQuestsProgress(questsType = None):
    return _PotapovDependenciesResolver.chooseList(questsType).progress


def getPotapovQuestsSelectProcessor(questsType = None):
    return _PotapovDependenciesResolver.chooseList(questsType).selectProcessor


def getPotapovQuestsRefuseProcessor(questsType = None):
    return _PotapovDependenciesResolver.chooseList(questsType).refuseProcessor


def getPotapovQuestsRewardProcessor(questsType = None):
    return _PotapovDependenciesResolver.chooseList(questsType).rewardsProcessor


def sortWithQuestType(items, key, questsType = None):
    return _PotapovDependenciesResolver.chooseList(questsType).sorter(items, key=key)


def getSortedTableData(tableData):
    return formatters.packVehiclesList(*caches.sortVehTable(tableData.tableID, tableData.buttonID, tableData.sortingDirection, int(tableData.nation), int(tableData.vehType), int(tableData.level), tableData.cbSelected, tableData.isAction))


_questBranchToTabMap = {PQ_BRANCH.REGULAR: QUESTS_ALIASES.SEASON_VIEW_TAB_RANDOM,
 PQ_BRANCH.FALLOUT: QUESTS_ALIASES.SEASON_VIEW_TAB_FALLOUT}

def getTabAliasByQuestBranchID(branchID):
    return _questBranchToTabMap[branchID]


def getTabAliasByQuestBranchName(branchName):
    return getTabAliasByQuestBranchID(PQ_BRANCH.NAME_TO_TYPE[branchName])


def getCarouselAwardVO(bonuses, isReceived = False):
    """ Generate award VOs for carousel.
    
    :param bonuses: list of bonuses (instances of gui.server_events.SimpleBonus).
    :param isReceived: flag describing whether this is 'already received' context.
    """
    result = []
    for bonus in bonuses:
        if not bonus.isShowInGUI():
            continue
        result.extend(bonus.getCarouselList(isReceived))

    while len(result) % _AWARDS_PER_PAGE != 0 and len(result) > _AWARDS_PER_PAGE:
        result.append({})

    return result


@async
@process('updating')
def getPotapovQuestAward(quest, callback):
    """ Display special tankwoman award window.
    """
    from gui.server_events.events_dispatcher import showTankwomanAward
    tankman, isMainBonus = quest.getTankmanBonus()
    needToGetTankman = quest.needToGetAddReward() and not isMainBonus or quest.needToGetMainReward() and isMainBonus
    if needToGetTankman and tankman is not None:
        for tmanData in tankman.getTankmenData():
            showTankwomanAward(quest.getID(), tmanData)
            break

        result = None
    else:
        result = yield getPotapovQuestsRewardProcessor()(quest).request()
    callback(result)
    return


def questsSortFunc(a, b):
    """ Sort function for common quests (all except potapov, club and motive).
    """
    res = cmp(a.isCompleted(), b.isCompleted())
    if res:
        return res
    res = cmp(a.getType() == constants.EVENT_TYPE.FORT_QUEST, a.getType() == constants.EVENT_TYPE.FORT_QUEST)
    if res:
        return -res
    res = cmp(a.getPriority(), b.getPriority())
    if res:
        return res
    return cmp(a.getUserName(), b.getUserName())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\lobby\server_events\events_helpers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:50:54 St�edn� Evropa (b�n� �as)
