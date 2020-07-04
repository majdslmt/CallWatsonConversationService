class CallWatson(restful.Resource):
    def get(self,question):
    
        from watson_developer_cloud import ConversationV1
        conversation = ConversationV1(username = '', password = '', version = '')
        context = {}
        
        
        workspace_id = ''
        response = conversation.message(
        workspace_id=workspace_id,
        message_input={'text':question},
        context=context)
        
        result = response.get('entities')
        return (result)
