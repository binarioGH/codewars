#-*-coding: utf-8-*-

def format_duration(time):
	if time == 0:
		return "now"
	years = int(time / 31536000)
	time -= years * 31536000
	days = int(time / 86400)
	time -= days * 86400
	hours = int(time / 3600)
	time -= hours * 3600
	minutes = int(time/60)
	time -= minutes * 60
	seconds = time%60
	string = []
	if years:
		string.append("{} year{}".format(years, "s" if years > 1 else ""))
	
	if days:
		string.append("{} day{}".format(days, "s" if days > 1 else ""))
	
	if hours:
		string.append("{} hour{}".format(hours, "s" if hours > 1 else ""))
	
	if minutes:
		string.append("{} minute{}".format(minutes, "s" if minutes > 1 else ""))

	if seconds:
		string.append("{} second{}".format(seconds, "s" if seconds > 1 else ""))
	
	readable = ""
	for chunk in string:
		if chunk == string[-1] and chunk != string[0]:
			readable += " and {}".format(chunk)
		else:
			if chunk == string[0]:
				readable += chunk
			else:
				readable += ", {}".format(chunk)
	return readable





def main():
	time = int(input("Input the seconds:"))
	readable = format_duration(time)
	print(readable)


if __name__ == '__main__':
	main()