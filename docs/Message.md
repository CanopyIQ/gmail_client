# Message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history_id** | **str** | The ID of the last history record that modified this message. | [optional] 
**id** | **str** | The immutable ID of the message. | [optional] 
**internal_date** | **str** | The internal message creation timestamp (epoch ms), which determines ordering in the inbox. For normal SMTP-received email, this represents the time the message was originally accepted by Google, which is more reliable than the Date header. However, for API-migrated mail, it can be configured by client to be based on the Date header. | [optional] 
**label_ids** | **list[str]** | List of IDs of labels applied to this message. | [optional] 
**payload** | [**MessagePart**](MessagePart.md) | The parsed email structure in the message parts. | [optional] 
**raw** | **str** | The entire email message in an RFC 2822 formatted and base64url encoded string. Returned in messages.get and drafts.get responses when the format&#x3D;RAW parameter is supplied. | [optional] 
**size_estimate** | **int** | Estimated size in bytes of the message. | [optional] 
**snippet** | **str** | A short part of the message text. | [optional] 
**thread_id** | **str** | The ID of the thread the message belongs to. To add a message or draft to a thread, the following criteria must be met:  - The requested threadId must be specified on the Message or Draft.Message you supply with your request.  - The References and In-Reply-To headers must be set in compliance with the RFC 2822 standard.  - The Subject headers must match. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


