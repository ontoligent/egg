# EGG, an Entity Graph Generator

import pandas as pd

class EntityElementIndex(object):

	filename			  	= ''
	dataframe			  	= object
	element_id_col		  	= 'element_id'
	element_class_col	  	= 'element_class'
	entity_id_col		  	= 'entity_id'
	entity_class_col	  	= 'entity_class'
	default_element_class 	= 'element'
	default_entity_class  	= 'entity'
	
	def load_csvfile(self,filename):
		self.filename = filename
		self.dataframe = pd.read_csv(self.filename)        


class EntityGraphConfig(object):
	
	middle_term_col 			= 'element_id'
	subject_term_col 			= 'entity_id'
	predicate_term_col			= 'entity_id'
	subject_term_filter_col 	= 'entity_class'
	predicate_term_filter_col 	= 'entity_class'
	subject_term_filter_set		= set({})
	predicate_term_filter_set 	= set({})
	

class EntityGraph(object):
	index	= object
	config  = object
	graph	= {'nodes': object, 'edges': object} 
	
	def generate_graph(self):
		
		# Get objects 
		df 	= self.index.dataframe
		cfg	= self.config
		
		# Get configs
		m  = cfg.middle_term_col # Middle Term
		s  = cfg.subject_term_col # Subject 
		p  = cfg.predicate_term_col # Predicate
		sf = cfg.subject_term_filter_col
		sv = cfg.subject_term_filter_set
		pf = cfg.predicate_term_filter_col
		pv = cfg.predicate_term_filter_set
		
		# Create left and right tables for join and make graph
		S = df[[s,m]][df[sf].isin(sv)] # Subjects
		P = df[[p,m]][df[pf].isin(pv)] # Predicates

		# Create node array
		N = pd.concat([S[s],P[p]])
		N = pd.unique(N.values.ravel())
		
		# Create edges 
		E = pd.merge(S,P,on=m)
		E.columns = ['s','m','p']
		E = E[['s','p']][E.s != E.p].drop_duplicates().sort('s')
		
		# But may want to count repeats?
				
		# Remove reverse edges
		
		# Remove duplicates
				
		self.graph = {'nodes':N, 'edges':E}


class EntityGraphViz(object):

	def set_graph(self, graph_obj):
		return 1

	
if __name__ == '__main__':
	
	my_root = '/Users/rca2t/Dropbox/PLAY/egg/demo/'
	my_demo ='faulkner.csv' 

	# Create an object from the index file
	idx = EntityElementIndex()
	idx.load_csvfile(my_root + my_demo)
	idx.element_id_col 			= 'element_id'
	idx.entity_id_col 			= 'entity_id'
	idx.element_class_col 		= 'element_class'
	idx.entity_class_col 		= 'entity_class'

	# Define parameters for the graph to generate from the index object
	cfg = EntityGraphConfig()
	cfg.middle_term_col 			= 'element_id'
	cfg.subject_term_col 			= 'entity_id'
	cfg.predicate_term_col 			= 'entity_id'
	cfg.subject_term_filter_col 	= 'entity_class'
	cfg.predicate_term_filter_col	= 'entity_class'
	cfg.subject_term_filter_set 	= {'character'}
	cfg.predicate_term_filter_set 	= {'location'}
	
	# Create the graph object
	g 			= EntityGraph()
	g.index 	= idx
	g.config 	= cfg
	g.generate_graph()
	print g.graph['edges']
	print "DONE"