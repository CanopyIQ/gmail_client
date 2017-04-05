# VacationSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_auto_reply** | **bool** | Flag that controls whether Gmail automatically replies to messages. | [optional] 
**end_time** | **str** | An optional end time for sending auto-replies (epoch ms). When this is specified, Gmail will automatically reply only to messages that it receives before the end time. If both startTime and endTime are specified, startTime must precede endTime. | [optional] 
**response_body_html** | **str** | Response body in HTML format. Gmail will sanitize the HTML before storing it. | [optional] 
**response_body_plain_text** | **str** | Response body in plain text format. | [optional] 
**response_subject** | **str** | Optional text to prepend to the subject line in vacation responses. In order to enable auto-replies, either the response subject or the response body must be nonempty. | [optional] 
**restrict_to_contacts** | **bool** | Flag that determines whether responses are sent to recipients who are not in the user&#39;s list of contacts. | [optional] 
**restrict_to_domain** | **bool** | Flag that determines whether responses are sent to recipients who are outside of the user&#39;s domain. This feature is only available for G Suite users. | [optional] 
**start_time** | **str** | An optional start time for sending auto-replies (epoch ms). When this is specified, Gmail will automatically reply only to messages that it receives after the start time. If both startTime and endTime are specified, startTime must precede endTime. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


