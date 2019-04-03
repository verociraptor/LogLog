import csv
import math

class LogLogPlugin:
	def input(self, filename):
		self.myfile = filename

	def run(self):
		file = open(self.myfile, 'r')
		csv_reader = csv.reader(file)
		next(csv_reader)
		self.new_xdata = []
		self.new_ydata = []

		for row in csv_reader:
			self.new_xdata.append(math.log10(float(row[0])))
			self.new_ydata.append(math.log10(float(row[1])))

	
	def output(self, filename):
		new_csvfile = open(filename, mode="w")
		writer = csv.writer(new_csvfile, delimiter=",")
		writer.writerow(['x','y'])

		for new_x, new_y in zip(self.new_xdata, self.new_ydata):
			writer.writerow([new_x, new_y])