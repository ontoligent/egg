# Synopsis

Takes a csv file that maps semantic entities to document elements and 
generates an entity graph following the common container correlation 
pattern (Alvarado 2015). This graph may then be analyzed for its network 
properties of visualized in a variery of ways.

# Desing Notes

* Didactic code, i.e. verbose. Could have been written as one-liners.

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
      load_file
      set_element_id_col
      set_element_class_col
      set_entity_id_col
      set_entity_class_col
      set_default_element_class
      set_default_entity_class
      get_row_count
      get_col_count
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
      
