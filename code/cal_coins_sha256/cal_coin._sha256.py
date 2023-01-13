import json

import hashlib

# fw = open('coin_id_4','w')
# fw = open('coin_symbol_4','w')

# with open('coins_sumbol_4', 'r') as fcc_file:
# 	fcc_data = json.load(fcc_file)

# 	for i in range(len(fcc_data)):
# 		out = fcc_data[i]['id']
# 		print("%s" % out)
# 		print(out, file=fw)


fw = open('coin_id_hash_4','w')
# fw = open('coin_symbol_hash_4','w')

f = open("coin_id_4")               # 返回一个文件对象 
# f = open("coin_symbol_4")               # 返回一个文件对象 
lines = f.readlines()

for line in lines:
	print(line)
	line = line.replace('\n', '')
	c = line.encode()
	s = hashlib.sha256()
	s.update(c)
	out = s.hexdigest()
	print(out)
	print(out, file=fw)

f.close()
fw.close()


# 74de611122e4f8089e3bfd991fb4e77c60e6c02cf02d6ca078597a5a441b908b
# c0c51bfda648a9ffba80a2a3016e13af1c02f2402bd8d9b93fa93f4243f6c12e
# a1d1d92deeeda357bf6fc6503e8243a178eeb1a2d548bb1cb03febadb9f6d092
