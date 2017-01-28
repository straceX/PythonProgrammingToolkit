#!/usr/bin/python

def print_file_type_md5( file_path, file_type ):
	file_directory = os.path.abspath("apk")
	paths_to_hash = []

	for file in os.listdir(file_path):
    	if file.endswith(file_type):
    		paths_to_hash.append(file)

	for path in paths_to_hash:
    	hash = hashlib.md5(open(path, 'rb').read()).hexdigest()
    	print 'hash: {0} for path: {1}'.format(hash, path)
	
	return;

