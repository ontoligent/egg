'''
EGG, an Entity Graph Generator
'''

import pandas as pd

class EntityElementIndex(object):

	filename              = ''
	dataframe             = ''
	element_id_col        = 'element_id'
	element_class_col     = 'element_class'
	entity_id_col         = 'entity_id'
	entity_class_col      = 'entity_class'
	default_element_class = 'element'
	default_entity_class  = 'entity'
	
	def set_csvfile(self,filename):
		self.filename = filename
		self.dataframe = pd.read_csv(self.filename)
		
	def set_element_id_col(self,colname):
		self.element_id_col = colname

	def set_element_class_col(self,colname):
		self.element_class_col = colname

	def set_entity_id_col(self,colname):
		self.entity_id_col = colname

	def set_entity_class_col(self,colname):
		self.entity_class_col = colname

	def set_default_element_class(self,classname):
		self.default_element_class = classname

	def set_default_entity_class(self,classname):
		self.default_entity_class = classname
		
	def get_dataframe(self):
		return self.dataframe

	def get_element_classes(self):
		return 1

	def get_distinct_entity_ids(self):
		return 1

	def get_distinct_element_ids(self):
		return 1
		
	def get_dataframe(self):
		return self.dataframe


class EntityGraphConfig(object):

	def set_middle_term_col(self,colname):
		return 1

	def set_subject_term_col(self,colname):
		return 1

	def set_object_term_col(self,colname):
		return 1

	def set_subject_term_filter_col(self,colname):
		return 1

	def set_object_term_filter_col(self,colnanme):
		return 1

	def set_subject_term_filter_vals(self,vals):
		return 1

	def set_object_term_filter_vals(self,vals):
		return 1

	def get_config(self):
		return 1


class EntityGraph(object):

	def set_index(self, index_obj):
		return 1

	def set_config(self, config_obj):
		return 1

	def generate_graph(self):
		return 1

	def get_properties(self):
		return 1


class EntityGraphViz(object):

	def set_graph(self, graph_obj):
		return 1

	
if __name__ == '__main__':
	my_root = '/Users/rca2t/Dropbox/PLAY/egg/demo/'
	my_demo ='charrette.csv' 
	idx = EntityElementIndex()
	idx.set_csvfile(my_root + my_demo)
	idx.set_element_id_col('element_id')
	idx.set_entity_id_col('entity_id')
	idx.set_element_class_col('element_class')
	idx.set_entity_class_col('entity_class')
	df = idx.get_dataframe()
	print df
