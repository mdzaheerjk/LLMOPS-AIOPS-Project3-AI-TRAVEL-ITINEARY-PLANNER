from langchain_core.messages import HumanMessage,AIMessage
from src.chains.itinerary_chain import generate_itineary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages=[]
        self.city=""
        self.interests=[]
        self.itineary=""

        logger.info("Intilaized TravelPlanner instance")

    def set_city(self,city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=city))
            logger.info("City set sucesfully")
        except Exception as e:
            logger.error(f"error whiile setting city : {e}")
            raise CustomException("Failed to set city" , e)
        
    def set_interests(self,interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info("Interest also set sucesfully..")
        except Exception as e:
            logger.error(f"error whiile setting interests : {e}")
            raise CustomException("Failed to set interest" , e)
        
    def create_itineary(self):
        try:
            logger.info(f"Gnerating itineary for {self.city} and for interests : {self.interests}")
            itineary = generate_itineary(self.city,self.interests)
            self.itineary = itineary
            self.messages.append(AIMessage(content=itineary))
            logger.info("Itineary generated sucesffully..")
            return itineary
        except Exception as e:
            logger.error(f"error whiile creating itineary : {e}")
            raise CustomException("Failed to create itineary" , e)
