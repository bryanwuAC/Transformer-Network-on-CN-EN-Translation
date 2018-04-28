def read_file(file_path):
	print("Reading data:", file_path)
	file_data = []
	line_count = 0
	with open(file_path, mode = 'r', encoding = 'utf8') as file:
		for line in file:
			file_data.append(line.strip())
	return file_data

def clean_data(zh_data, en_data):
	print("Cleaning data...")
	assert len(en_data) == len(zh_data)
	zh_dict = {}
	clean_en_data = []
	clean_zh_data = []

	for i in range(len(zh_data)):
		zh_line = zh_data[i]
		en_line = en_data[i]

		if i % 100000 == 0:
			print ("Processed lines:", i)
		if zh_line in zh_dict:
			continue
		else:
			zh_dict[zh_line] = True
			clean_zh_data.append(zh_line)
			clean_en_data.append(en_line)

	assert len(en_data) == len(zh_data)
	return clean_zh_data, clean_en_data

def write_file(file_path, data):
	print("Writing data...")
	with open(file_path, mode = 'w', encoding = 'utf8') as file:
		for line in data:
			file.write("%s\n" % line)


ZH_PATH = "corpora/MultiUN.en-zh.zh"
EN_PATH = "corpora/MultiUN.en-zh.en"
ZH_OUT = "corpora/MultiUN.en-zh.zh-clean"
EN_OUT = "corpora/MultiUN.en-zh.en-clean"
CLEAN_RANGE = 300000

zh_data = read_file(ZH_PATH)
en_data = read_file(EN_PATH)

clean_zh_data, clean_en_data = clean_data(zh_data, en_data)

write_file(ZH_OUT, clean_zh_data)
write_file(EN_OUT, clean_en_data)
