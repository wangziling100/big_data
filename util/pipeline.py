from sklearn.pipeline import Pipeline
import const


class simple_pipeline(Pipeline):

    """
    a simple wrapper class of pipeline class in sklearn
    """

    const.feature_selection = 1


    def __init__(self, strategy=None):
        self.strategy = strategy
        const.feature_selection = 0

        pass






if __name__ == '__main__':
    mypipe = simple_pipeline()
