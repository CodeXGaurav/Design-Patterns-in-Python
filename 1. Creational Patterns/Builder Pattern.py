
class Aircraft:
	pass

class Boeing747(Aircraft):

	def __init__(self):
		self.engine = None
		self.wings = None
		


class F16(Aircraft):
	def __init__(self):
		self.engine = None
		self.wings = None
		

class Aircraftbuilder:

	def buildEngine(self):
		pass

	def buildWIngs(self):
		pass

	def buildCockpit(self):
		pass

	

class F16builder(Aircraftbuilder):

	# @Override
	def buildEngine(self):
		self.f16.engine = "f16 engine"
		return self

	# @Override
	def buildWings(self):
		self.f16.wings = "f16 wings"
		return self

	 #@Override
	def buildCockpit(self):
		self.f16 = F16()
		return self

	def getResult(self):
		return self.f16

	


class Boeing747builder(Aircraftbuilder):
	

	# @Override
	def buildEngine(self):
		self.boeing747.engine = "boeing engine"
		return self

	# @Override
	def buildWings(self):
		self.boeing747.wings = "boeing wings"
		return self

	 #@Override
	def buildCockpit(self):
		self.boeing747 = Boeing747()
		return self



	def getResult(self):
		return self.boeing747



class Director:

	
	# def __init__(self, aircraft_builder):
	# 	self.aircraft_builder = aircraft_builder
 
	def set_AB(self, aircraft_builder):
		self.aircraft_builder = aircraft_builder
 

	def construct(self, isPassenger):
		aircraft_builder = self.aircraft_builder
		#aircraft_builder.buildCockpit()
		#aircraft_builder.buildEngine()
		#aircraft_builder.buildWings()


		aircraft_builder.buildCockpit().buildEngine().buildWings()

	  
 
class Client:

	def create_name(self):
		director = Director()

		f16Builder = F16builder()
		director.set_AB(f16Builder)
		director.construct(True)

		f16 = f16Builder.getResult()
		print(f16.engine, f16.wings)
		
		boeing747builder = Boeing747builder() 
		director.set_AB(boeing747builder)			
		director.construct(True)

		boeing747 = boeing747builder.getResult()
		print(boeing747.engine, boeing747.wings)
		#print(Boeing747builder.boeing747)	



if __name__ == '__main__':

	client = Client()
	client.create_name()

