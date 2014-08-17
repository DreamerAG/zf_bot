# coding=utf-8
import logging
#import pdb
from game_state.game_types import GameWoodGrave, GameWoodGraveDouble,\
    GamePickItem, GameWoodTree, GameStone, GameGainItem, GamePickup
from game_state.game_event import dict2obj, obj2dict
from game_actors_and_handlers.base import BaseActor

logger = logging.getLogger(__name__)

class PirateTreeCut(BaseActor):

    def get_object_type(self):
        return "chop"

    def perform_action(self):
        resources = self._get_game_location().get_all_objects_by_type(
                    self.get_object_type()
                )
        enemies = self._get_game_location().get_all_objects_by_type("pirateEnemy")
        # пиратские острова : Остров сокровищ , Таинственный , Жуткий , Северный полюс , Остров сокровищ , Древний
        pirate_locs_id = ["exploration_isle1_random","exploration_isle2_random","exploration_isle3_random","exploration_snow1","exploration_isle1_1","exploration_isle4_random"]
        # Не понятно, что это за острова в списке ???? - Пушистый 1,2,3 и Подземелье 1,2
        #"exploration_furry1","exploration_furry2","exploration_furry3","exploration_isle_un1_1","exploration_isle_un1_2"

        instruments = [] # переменная для инструментов

        _loc = self._get_game_state().get_game_loc().get_location_id() # текущая локация
        if not enemies:
            open('.\counts\\SilverHit.txt','w').write('')
			
        for object in self._get_game_location().get_game_objects():
            if object.type == 'pirateEnemy':
                hitsilver = open('.\counts\\SilverHit.txt','r').read()
                if not str(object.id) in hitsilver:
                    gain_event = {"action":"hit","objId":object.id,"type":"pirateEnemy"}
                    open('.\counts\\SilverHit.txt','a').write(str(object.id)+',')
                    self._get_events_sender().send_game_events( [gain_event] )
                    counthealt = object.health-1
                    logger.info(u'БЬЮ СИЛЬВЕРА %s осталось добить %d раз(а)'%(str(object.id),counthealt))
        if resources:
          if _loc not in pirate_locs_id:
            st_items = self._get_game_state().get_state().storageItems # Предметы на складе
            for item in list(st_items):
              if hasattr(item, "item"):
                if item.item == ('@CHOP_MACHETE'): #мачете
                  instruments.append(dict2obj({"item":"@CHOP_MACHETE", "count": item.count}))
                if item.item == ('@CHOP_AXE'): #топор
                  instruments.append(dict2obj({"item":"@CHOP_AXE", "count": item.count}))
                if item.item == ('@CHOP_HAMMER'): #кирка
                  instruments.append(dict2obj({"item":"@CHOP_HAMMER", "count": item.count}))
          else: instruments = self._get_game_state().get_state().pirate.instruments

#Старый модуль, работает с ошибками
          for resource in resources:
            resource_name = self._get_item_reader().get_name(resource)
            tool_needed = resource.chopCount
            type_of_res = resource.item
            type_of_instrument = self._get_item_reader().get(type_of_res).chopInstrumentType
            for tool in instruments:
                name_tool = self._get_item_reader().get_name(tool)
                if self._get_item_reader().get(tool.item).chopInstrumentType == type_of_instrument and tool.count >= tool_needed:
                    enemy_here = 0
                    if enemies:
                        for enemy in enemies:
                            if(((enemy.x - resource.x)**2+(enemy.y - resource.y)**2)**0.5 <= 15):
                                enemy_here = 1
                                break
                    if(enemy_here == 1):
                        self._get_game_location().remove_object_by_id(resource.id)
                        logger.info(u"Сильвер мешает вырубке " + resource_name)
                        break
                    #А что черепа никому не нужны? Почему никто не рубит камни по 100 сериями по 50?
                    #Я обычно валуны рублю вручную в 2 этапа - 60 и 40. Зачастую на 60 падает от 2 до 6 черепов (рандом, мать его). 
                    #А на 40 уже так, что выпадет. Когда целиком или по 50, то зачастую порожняки сыпят.
                    #ЗЫ. Посмотрел сейчас, код не правильный будет на разбиение больших камней. 
                    #Нужно переделывать, кто использует. В данном случае вроде вырубает половину и просто удаляет оставшееся с острова. 
                    #Необходимо 2-ю рубку делать.
                    #if tool_needed == 100:
                    #    tool_needed = 50 
                    # Рубим мелкими партиями, по 4 шт, для фейков
                    #if tool_needed > 8:
                    #    tool_needed = 4 


                    gain_event = {"type":"chop","objId":resource.id,"instruments":{self._get_item_reader().get(tool.item).id:tool_needed},"action":"chop"}
                    logger.info(u"Рубим " + resource_name + u" с помощью " + str(tool_needed) + u" " + name_tool)
                    self._get_events_sender().send_game_events( [gain_event] )
                    self._get_game_location().remove_object_by_id(resource.id)
                    tool.count -= tool_needed
                    break
        else:
            logger.info("Не осталось ресурсов для добычи")
        resources = self._get_game_location().get_all_objects_by_type("pirateCaptureObject")
        if resources:
            for resource in resources:
                resource_name = self._get_item_reader().get_name(resource)
                enemy_here = 0
                if enemies:
                    for enemy in enemies:
                        if(((enemy.x - resource.x)**2+(enemy.y - resource.y)**2)**0.5 <= 15):
                            enemy_here = 1
                            break
                if(enemy_here == 1):
                    self._get_game_location().remove_object_by_id(resource.id)
                    logger.info(u"Сильвер мешает взять " + resource_name)
                    continue
                gain_event = {"type":"pirateCapture","objId":resource.id,"action":"capture"}
                logger.info(u"Открываем " + resource_name)
                self._get_events_sender().send_game_events( [gain_event] )
                self._get_game_location().remove_object_by_id(resource.id)
        else:
            logger.info("Нет неоткрытых сокровищ")







#Новый модуль, нужно проверить
'''
          for resource in resources:
            resource_name = self._get_item_reader().get_name(resource)
            tool_needed = resource.chopCount
            type_of_res = resource.item
            type_of_instrument = self._get_item_reader().get(type_of_res).chopInstrumentType
            _i = -1
            for tool in instruments:
                _i += 1
                name_tool = self._get_item_reader().get_name(tool)
                if self._get_item_reader().get(tool.item).chopInstrumentType == type_of_instrument and tool.count >= tool_needed:
                    dell = instruments.pop(_i)
                    enemy_here = 0
                    if enemies:
                        for enemy in enemies:
                            if(((enemy.x - resource.x)**2+(enemy.y - resource.y)**2)**0.5 <= 15):
                                enemy_here = 1
                                break
                    if(enemy_here == 1):
                        self._get_game_location().remove_object_by_id(resource.id)
                        logger.info(u"Сильвер мешает вырубке " + resource_name)
                        break
                    if tool_needed == 100:
                        tool_needed = 50
                    gain_event = {"type":"chop","objId":resource.id,"instruments":{self._get_item_reader().get(tool.item).id:tool_needed},"action":"chop"}
                    logger.info(u"Рубим " + resource_name + u" с помощью " + str(tool_needed) + u" " + name_tool)
                    self._get_events_sender().send_game_events( [gain_event] )
                    self._get_game_location().remove_object_by_id(resource.id)
                    dell.count -= tool_needed
                    instruments.insert(_i,dell)
                    break
                    
        else:
            logger.info("Не осталось ресурсов для добычи") '''





