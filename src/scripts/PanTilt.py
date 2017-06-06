import pantilthat
import time

class PanTilt(object):

	current_tilt_angle=0
	current_pan_angle=0

	offset_pan=0
	offset_tilt=0
	offset_tilt_step=0.5;
	offset_pan_step=0.5;

	MAX_PAN=90
	MAX_TILT=90

	def __init__(self):
		self.center()


	def pan(self,a):
		self.current_pan_angle=a+self.offset_pan
		self.refreshPan()

	def tilt(self,a):
		self.current_tilt_angle=a+self.offset_tilt
		self.refreshTilt()		

	def refreshTilt(self):
		# self.current_tilt_angle=self.current_tilt_angle+self.offset_tilt
		if (self.current_tilt_angle>self.MAX_TILT):
			self.current_tilt_angle=self.MAX_TILT
		if (self.current_tilt_angle<-self.MAX_TILT):
			self.current_tilt_angle=-self.MAX_TILT
		pantilthat.tilt(self.current_tilt_angle)

	def refreshPan(self):
		# self.current_pan_angle=self.current_pan_angle+self.offset_pan
		if (self.current_pan_angle>self.MAX_PAN):
			self.current_pan_angle=self.MAX_PAN
		if (self.current_pan_angle<-self.MAX_PAN):
			self.current_pan_angle=-self.MAX_PAN
		pantilthat.pan(self.current_pan_angle)

	def panTilt(self,pan,tilt):
		self.pan(pan)
		self.tilt(tilt)

	def center(self):
		self.pan(0)
		self.tilt(0)		

		"""
		to increase the offset step by step if true
		"""
	def increaseOffset(self,pan=0,tilt=0):

		if pan>0:
			self.offset_pan=self.offset_pan+self.offset_pan_step
			if (self.offset_pan>self.MAX_PAN/2): self.offset_pan=self.MAX_PAN/2
			self.refreshPan()
			#time.sleep(0.5)
		elif pan<0:
			self.offset_pan=self.offset_pan-self.offset_pan_step
			if (self.offset_pan<-self.MAX_PAN/2): self.offset_pan=-self.MAX_PAN/2
			self.refreshPan()
			#time.sleep(0.5)


		if tilt>0:
			self.offset_tilt=self.offset_tilt+self.offset_tilt_step
			if (self.offset_tilt>self.MAX_TILT/2): self.offset_tilt=self.MAX_TILT/2
			self.refreshTilt()
			#time.sleep(0.5)
		elif tilt<0:
			self.offset_tilt=self.offset_tilt-self.offset_tilt_step
			if (self.offset_tilt<-self.MAX_TILT/2): self.offset_tilt=-self.MAX_TILT/2
			self.refreshTilt()
			#time.sleep(0.5)
