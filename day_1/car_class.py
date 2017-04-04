class Car(object):
	def __init__(self,name="General",model="GM",speed=0, **kwargs): 
		"""Return a new Car object."""
		self.type = car_type
		self.model = car_model
		self.name = car_name
		self.speed = speed
		self.wheels = wheels
		self.doors = doors


		if name in ['Porsche','Koenigsegg']:
			doors =4
		else:
			doors =8
		if car_type == 'trailer':
			wheels =8
		else:
			wheels =4
	def is_saloon(self):
		if car_type is not 'trailer':
			car_type == 'saloon'
			return True
		return False
	def drive(self,speed):
		if speed == 3:
			Car.speed = 1000
		elif speed ==7:
			Car.speed == 77
		return self