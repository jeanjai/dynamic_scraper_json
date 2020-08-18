from commands import base
import json
import pdb


class scraper():
    
    data = [[]]
    data_headers = data[0]
    row = []
    curent_columns = -1

    def __init__(self):
        with open('json_exceptions/multiple_different_result_length.json') as json_file:
            self.jsonData = json.load(json_file)

        self.browser = base()
        self.compilePageResults([{
            "parent_id": "_root_",
            "is_link": True,
            "has_child": True,
            "results": self.jsonData["start_urls"]
        }])
        print(self.data)


    def runPageActions(self, parent_id):
        page_data = []
        
        for action in self.jsonData["actions"]:
            if parent_id in action["parent"]:
                page_data.append({
                    "parent_id": action["id"],
                    "is_link": action["type"] == "SelectorLink",
                    "has_child": self.hasChild(action["id"]),
                    "results": self.runAction(action)
                })

        self.compilePageResults(page_data)


    def compilePageResults(self, page_data):
        for action_data in page_data:
            for i, result in enumerate(action_data["results"]):
                self.row.append([action_data["parent_id"], result])
                
                if action_data["has_child"]:
                    if action_data["is_link"]:
                        self.browser.visit(result)
                    self.runPageActions(action_data["parent_id"])
                
                else:
                    self.exportResults(self.row)
                    self.row.pop()

        if page_data[0]["parent_id"] != "_root_":
            self.row.pop()


    def exportResults(self, row):
        export_row = [''] * len(self.data_headers)

        # result = [parent, value]
        for result in row:
            result_header = result[0]
            result_value = result[1]

            try:
                index = self.data_headers.index(result_header)
                export_row[index] = result_value
            
            # if result_header is not in data_headers
            except ValueError as e:
                self.data_headers.append(result_header)
                export_row.append(result_value)
        
        self.data.append(export_row)

    
    def hasChild(self, parent):
        for action in self.jsonData["actions"]:
            if parent in action["parent"]:
                return True

        return False


    def runAction(self, action):
        if action["type"] == "enterText":
            self.browser.write(action["selector"],action["value"])
        
        elif action["type"] == "SelectorText":
            if action["multiple"]:
                return self.browser.getValues(action["selector"])
            else:
                return self.browser.getValue(action["selector"])
        
        elif action["type"] == "getAttribute":
            if action["multiple"]:
                return self.browser.getAttributes(action["selector"], action["attribute"])
            else:
                return self.browser.getAttribute(action["selector"], action["attribute"])
    
        elif action["type"] == "click":
            self.browser.click(action["selector"])

        elif action["type"] == "SelectorLink":
            if action["multiple"]:
                return self.browser.getLinks(action["selector"])
            else:
                return self.browser.getLink(action["selector"])

        # elif action["type"] == "ifElse":
            # runTypes(action["if"])

        # elif action["type"] == "prioritizeSelector":
            # runTypes(action["if"])

        else:
            print("Please enter a valid type")

    def __exit__(self):
        self.browser.end()


scraper()