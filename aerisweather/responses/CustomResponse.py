

class CustomResponse:
    """ Defines an object to handle a response from a custom or unknown endpoint. This response class is intended
        to provide support handling newer endpoints that may not yet be included in the production release of
        the library.

        Since this object will built on the fly, aut-completion tools like Intellisense won't be able to help
        out with the class members, but all dot notation is still applicable in the code. However, if you use
        typing to specify the various object types while declaring them, the code following the type definition
         will be recognized. Example:
                EndpointType.custom = "rivers/gauges"
                rg_list = awx.request(endpoint=Endpoint(endpoint_type=EndpointType.CUSTOM,
                                                        location=RequestLocation(postal_code="57101")))
                rg = rg_list[0]
                assert type(rg) is CustomResponse
                profile = rg.profile  # type: AerisProfileRiversGauges
                crests = profile.crests  # type: RiversCrests
                recent = crests.recent  # type: [RiversCrestsRecent]
                assert recent[0].heightFT is not None
    """

    def __init__(self, json_data=None):
        """ Constructor """

        self.parse_dict(self, json_data)

    def parse_dict(self, parent_obj: object, dic: dict):

        for attr, value in dic.items():  # walk through the dictionary

            if type(value) is dict:
                obj_dict = self.make_object(attr)  # store the dict contents
                self.parse_dict(obj_dict, value)  # parse the contents
                setattr(parent_obj, attr, obj_dict)  # assign the completed obj to its parent

            elif type(value) is list:
                list_contents = []  # create a new list to hold the deserialized contents of the list

                for item in value:
                    obj_item_parent = self.make_object("")  # store the list contents

                    if type(item) is dict:
                        self.parse_dict(obj_item_parent, item)  # nested dict
                    else:
                        setattr(obj_item_parent, attr, item)  # assign the completed obj to its parent

                    list_contents.append(obj_item_parent)  # add the item to the new list

                setattr(parent_obj, attr, list_contents)  # save the new list to the parent
            else:
                setattr(parent_obj, attr, value)  # assign the completed obj to its parent

    def make_object(self, name: str) -> object:
        body = dict(__doc__='docstring', __name__=name, __module__='modname')
        cls = type(name, (object,), body)
        return cls
