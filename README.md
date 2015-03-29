# Synopsis

Takes a CSV file that maps *semantic entities* to *document elements* and 
generates an *entity graph* following the *common container correlation* 
pattern (Alvarado 2015). This graph may then be analyzed for its network 
properties of visualized in a variery of ways.

# Design Notes

* Didactic code, i.e. verbose. Could have been written as one-liners.

# Background Information

## What is an entity graph?

### Common Container Correlation

### Data Model

### Mapping Entities and Elements to Ontologies	

### Examples of well known entity graphs include:
* Term/Document Frequency lists
* Knuth's Les Miserables
* Examples from TextScope
* Latour and Teil's Hume Machine

Other examples:
* Chacters names in paragraphs
* Iconographic elements in works of art

# Object Model

Objects:
  <pre>

  **EntityElementIndex**
    Description 
      A CSV file that contains an Entity to Element index
      Must contain at least two columns -- Entity ID and Element ID
      May also containt Entity Class and Element Class cols as well
      If the class columns are not present, a default type for each should be given
    Methods
      set_csvfile(csvfile)
      	csvfile = full path to a CSV file in the proper format
      set_element_id_col(colname)
      	colname = the name of the column that contains element IDs
      set_element_class_col(colname)
      	colname = the name of the column that contains element class values
      set_entity_id_col(colname)
				colname = the name of the column that contains entity IDs
      set_entity_class_col(colname)
      	colname = the name of the column that contains entity class values
      set_default_element_class(classname)
      set_default_entity_class(classname)
			get_dataframe
				Returns the pandas dataframe object for the CSV file
      get_element_classes
      get_distinct_entity_ids
      get_distinct_element_ids

  **EntityGraphConfig**
    Description
      Defines which cols and filters will be used to construct the graph
    Methods
      set_middle_term_col
      set_subject_term_col
      set_object_term_col
      set_subject_term_filter_col
      set_object_term_filter_col
      set_subject_term_filter_vals
      set_object_term_filter_vals
      get_config

  **EntityGraph**
    Description
    Methods
      set_index (object)
      set_config (object)
      generate_graph
      get_properties

  **EntityGraphViz**
    Methods
      set_graph (object)
</pre>      
      
