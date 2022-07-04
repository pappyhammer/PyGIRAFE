from cicada.analysis.cicada_analysis import CicadaAnalysis
from time import time


class CicadaCellAssVsIntervalsAnalysis(CicadaAnalysis):
    def __init__(self, config_handler=None):
        """
        """
        CicadaAnalysis.__init__(self, name="Epoch associated cell assemblies", family_id="Epochs",
                                short_description="Distribution of cell assemblies in epochs",
                                config_handler=config_handler,
                                accepted_data_formats=["CI_DATA"])

    def copy(self):
        """
        Make a copy of the analysis
        Returns:

        """
        analysis_copy = CicadaCellAssVsIntervalsAnalysis(config_handler=self.config_handler)
        self.transfer_attributes_to_tabula_rasa_copy(analysis_copy=analysis_copy)
        return analysis_copy

    def check_data(self):
        """
        Check the data given one initiating the class and return True if the data given allows the analysis
        implemented, False otherwise.
        :return: a boolean
        """
        super().check_data()

        self.invalid_data_help = "Not implemented yet"
        return False

        for session_index, session_data in enumerate(self._data_to_analyse):
            if session_data.DATA_FORMAT != "CI_DATA":
                self.invalid_data_help = f"Non CI_DATA format compatibility not yet implemented: " \
                                         f"{session_data.DATA_FORMAT}"
                return False

        return True

    def set_arguments_for_gui(self):
        """

        Returns:

        """
        CicadaAnalysis.set_arguments_for_gui(self)

    def update_original_data(self):
        """
        To be called if the data to analyse should be updated after the analysis has been run.
        :return: boolean: return True if the data has been modified
        """
        pass

    def run_analysis(self, **kwargs):
        """
        testa
        :param kwargs:
          segmentation

        :return:
        """
        CicadaAnalysis.run_analysis(self, **kwargs)

        start_time = time()
        print("Cell assemblies vs intervals: coming soon...")
        n_sessions = len(self._data_to_analyse)
        self.update_progressbar(start_time, 100 / n_sessions)
