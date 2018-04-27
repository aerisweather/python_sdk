
import logging
from aenum import Enum


class AerisErrorLevel(Enum):
    INFO = "info"
    WARNING = "warning"
    NO_DATA = "warn_no_data"
    ERROR = "error"


class AerisError(OSError):
    """
    AerisError is a sub-type of OSError, but it doesn't share any of the implementation. It sets self.args for
    compatibility with other EnvironmentError subclasses, but args doesn't have the typical format with errno in
    slot 0 and strerror in slot 1.


    """
    def __init__(self, code: str, description: str, error_level: str):
        self.args = code, description
        self.__code = code
        self.__description = description
        self.__reason = code + ": " + description
        self.__response_json = ""
        self.__error_level = error_level

    def __str__(self) -> str:
        return self.__code + ": " + self.__description + "\n" + str(self.response_json)

    @property
    def code(self):
        return self.__code

    @ property
    def description(self):
        return self.__description

    @property
    def reason(self) -> str:
        return self.__reason

    @property
    def response_json(self) -> str:
        return self.__response_json

    @property
    def level(self) -> str:
        return self.__error_level

    @staticmethod
    def api_error(response_json):
        """ Takes the json str of an AerisAPI response and checks for errors or warnings.
            Returns an AerisError object or None """

        if response_json["success"] is False:
            logging.basicConfig(level=logging.ERROR)
            logger = logging.getLogger("Aeris API Error")

            if response_json["error"]["description"] is not None:
                err = AerisError(code=response_json["error"]["code"],
                                 description=response_json["error"]["description"],
                                 error_level=AerisErrorLevel.ERROR)
            else:
                err = AerisError(code="unknown",
                                 description="Unknown Error from Aeris API: ",
                                 error_level=AerisErrorLevel.ERROR)

            err.__response_json = response_json
            logger.error(str(err))

            return err
        else:
            # If we're here, success is true - but we need to check for warnings.
            if response_json["error"] is not None:
                # there must be some kind of warning
                logging.basicConfig(level=logging.WARNING)
                logger = logging.getLogger('Aeris API Warning')

                if response_json["error"]["code"] is not None:
                    # we got an error/warning code

                    if response_json["error"]["code"] == "warn_no_data":
                        # success is true, but there is no data
                        err = AerisError(code=response_json["error"]["code"],
                                         description=response_json["error"]["description"],
                                         error_level=AerisErrorLevel.NO_DATA)
                    else:
                        # success is true, and there is probably data, but there is also a warning
                        err = AerisError(code=response_json["error"]["code"],
                                         description=response_json["error"]["description"],
                                         error_level=AerisErrorLevel.WARNING)
                else:
                    # the error field had some data, but there is no code (prob no description either)
                    err = AerisError(code="unknown warning",
                                     description="Unknown Aeris API warning",
                                     error_level=AerisErrorLevel.WARNING)

                # log and return the warning
                logger.warning(str(err))

            return None
