-----------
Data format
-----------

In order to use CICADA, you will need to have data in a format compatible with the wrapper provided or
that you have written (instance of CicadaAnalysisFormatWrapper).

We provide a wrapper for NWB format so far. We will explain below how our NWB files are organized.

We also provide some scripts that allows to convert your data to NWB. You might have to write some code so it can
fit to your data format. This pre-processing module provides a plugin-like interface.

It's a Python pipeline aimed for analyzing calcium imaging data.

NWB Format
""""""""""

NWB stands for `Neurodata Without Borders: Neurophysiology (NWB:N) <https://www.nwb.org/>`_.

NWB is organized in different modules.

So far, here are the kind of data we have included in the NWB files:

* **Calcium imaging movies**: the movie is added in acquisitions as a TwoPhotonSeries instance.
  It is possible to either save the movie as an external file (keeping only the reference to the file path and name) or
  keeping the whole data. You can either add only the motion corrected movie or both the original and corrected one.
  If the xy translations from the correction are available, they can be added as a CorrectedImageStack instance.

* **ABF file**: abf allows to extract timestamps and to synchronize our different acquisitions
  (calcium imaging data, behavior movies, speed on treadmill, LFP signal, piezo). Timestamps are saved as
  TimeSeries instances in the acquisition module of NWB

* **ROIs**: ROIs are instances of ImageSegmentation added in our case as a processing module called "ophys". But the
  name could be changed as the wrapper will look for ImageSegmentation in all processing modules.

* **Cell type**: Cell type is added in RoiResponseSeries of the Fluorescence instance containing in the field control
  and control_descrption. Control is a 1d array (uint8) containing a code for each ROIs (each code represent a cell type)
  Control_description is a list of string (the length equals the number of cells),
  the string represents the cell type description.

* **Neuronal activity**: We have different type of neuronal activity.

    * **Raw fluorescence signal**: Added as RoiResponseSeries in an instance of Fluorescence itself
      in the data_interface list of NWB.

    * **Cell activity**: what we call raster dur, is a binary matrix (n_cells * n_frames), and indicate for
      any given cell at any given frame if the cell is active or not
      (corresponding to the rise time of fluorescence signal). The same format can be used to record spikes inference,
      a 1 indicating a spike.

* **Behavior movies**: are added as ImageSeries in the NWB acquisitions. To save memory, we only keep the external
  reference to the file. The name of our behaviors movies are such as f'behavior_cam_{cam_id}'. The timestamps
  of each frame are available as TimeSeries such as described in the abf file section.

* **Behavior Epochs**: (time intervals) are recorded as BehavioralEpochs added in NWB data interfaces.

* **Invalid times**: Invalid times are added as Invalid time intervals in the NWB.

* **Other Epochs**: Are added as TimeIntervals using the create_time_intervals method.


NWB pre-processing
""""""""""""""""""

The pre-processing procedure aims at converting your data in the NWB format.

To do so we explore directories, each session data is contained in a given directory that will also contain a
set of yaml files containing metadata and some configuration options.

To run the pre-processing you have to call the function convert_data_to_nwb() in
cicada.preprocessing.cicada_data_to_nwb, it takes 3 arguments:

* data_to_convert_dir (str): Absolute path to the directory containing all data
* default_convert_to_nwb_yml_file (str): Absolute path to the default YAML file to convert an NWB file
* nwb_files_dir (str): Absolute path to the directory where to save the nwb file created

In order to run through the directories that contains data to be converted, you can use the function
find_dir_to_convert() in from cicada.preprocessing.cicada_preprocessing_main which return a list of directories
contains at least a file for each given keywords with a specific extensions. In our case, we are using the keywords
[["session_data"], ["subject_data"]] with yaml extensions.

In each session directory, you should have two yaml files that will contain the metadata one regarding the subject,
the other the session. We will put some examples online soon.

Then the pre-processing is run according to the yaml configuration file that is passed as argument in
convert_data_to_nwb(). A default one is given in cicada.preprocessing with name pre_processing_default.yaml

You can make your own to fit your data.

Each step of the process is creating an instance of an implementation classes that inherit from ConvertToNWB
(see in convert_to_nwb.py).
You can create your own implementations.

Those classes are called in the order indicated in the yaml file in the order list.
The py file names that contains the classes should respect a strict rule with only lower case and an underscore (_)
added before a previously upper case letter. As example, ConvertBehaviorMovieToNWB will be in a file named
convert_behavior_movie_to_nwb.py

Then for each instance of ConvertToNWB inherited classes that will be used, you need to indicate which arguments
will be pass to the convert() methods.

Each entry of the yaml is the name of a class except for the entries order. So when the yaml will be read, we will
get a dictionary with all those entries as keys.

First of all, if you want the class to be run for several different types of inputs, you can put the configuration
for the class in a dict with key being numerical values (1, 2, etc...).

Then for each class, the entry in the yaml represents an argument (we will get it via the kwargs.get(arg_name) in
the convert() method). Depending on the data, here are the sub-fields:

* **Files**:

  * keyword: list of keywords, only the files with those keywords will be selected
  * keyword_to_exclude: list of keywords, only files with non of those keywords will be returned.
  * dir: if given, means the file will be searched in this/those directory(ies)
  * extension: only files with one of those extensions will be returned
  * value: if file with .mat or .npz files, if a value is given, then the field with value as key is passed
    as argument instead of the file name.

* **Values**:

  * value: if no keywords or extensions are given, the content of value will
    given to the argument.

* **Values from other classes**:

    * from_other_converter: indicates from which other instance of ConvertToNWB we want to extract a value.
    * value: name of the attribute from the other converter that we want to be put in the argument. The other
      converter need to be called before the current one.


With this yaml file you can then create your NWB file step by step from each kind of data you have.