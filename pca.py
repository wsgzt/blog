from numpy import *;
import Image;

def pca(data, dimen) :
	'''
	data:
		an array of sample, normalization processed. 
	dimen:
		dimension of the main component.
	'''
	# process the data.
	avgs = [];
	for d in data :
		avg = mean(d, axis=0);
		d -= avg;
		avgs.append(avg);
	
	# covariance matrix.	
	c = cov(data);

	# get eigenvalues and eigenvectors.
	values,vectors = linalg.eig(c);
	
	# get the max values.
	index = (argsort(values)[::-1])[0:dimen];
	values = values[:,index];
	vectors = vectors[:,index];

	new_data = dot(transpose(vectors), data);
	restore = dot(vectors, new_data);
	
	print '------ old ------'
	print data;
	print '------ new ------'
	print restore;
	print '-----------------'
	return restore,vectors;

# TEST
if __name__ == '__main__' :
	data = array([[1,5,6],[4,3,9],[4,2,9],[4,7,2]]);
	pca(data, 2);	
