import requests 

class HTTPConnector(object):
    '''
    This module is to make HTTP connections, trigger the requests and receive the response
    '''
    @staticmethod
    def get_instance(url,params,headers,body,method,apiKey,is_bulk_req):
        return HTTPConnector(url,params,headers, method)
    
    def __init__(self, url,params,headers,method):
        '''
        Constructor
        '''
        self.url=url
        self.req_headers=headers
        self.req_method=method
        self.req_params=params
        # self.api_key=apiKey
    
    def trigger_request(self):
        response=None
        if(self.req_method == APIConstants.REQUEST_METHOD_GET):
            #if(self.req_params!=None and self.req_params.length>0):
            #   self.url=self.url+'?'+self.get_request_params_as_string(self.req_params)
            response=requests.get(self.url, headers=self.req_headers,params=self.req_params,allow_redirects=False)
        elif(self.req_method==APIConstants.REQUEST_METHOD_PUT):
            response=requests.put(self.url, data=json.dumps(self.req_body),params=self.req_params,headers=self.req_headers,allow_redirects=False)
        elif(self.req_method==APIConstants.REQUEST_METHOD_POST):
            if self.file is None:
                response=requests.post(self.url,data=json.dumps(self.req_body), params=self.req_params,headers=self.req_headers,allow_redirects=False)
            else:
                response=requests.post(self.url, files=self.file,headers=self.req_headers,allow_redirects=False,data=self.req_body)
        elif(self.req_method==APIConstants.REQUEST_METHOD_DELETE):
            response=requests.delete(self.url,headers=self.req_headers,params=self.req_params,allow_redirects=False)
        return response
        

class APIConstants(object):
    '''
    This module holds the constants required for the client library
    '''
    ERROR="error"
    REQUEST_METHOD_GET="GET"
    REQUEST_METHOD_POST="POST"
    REQUEST_METHOD_PUT="PUT"
    REQUEST_METHOD_DELETE="DELETE"