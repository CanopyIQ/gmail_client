# gmail_client.UsersApi

All URIs are relative to *https://www.googleapis.com/gmail/v1/users*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gmail_users_drafts_create**](UsersApi.md#gmail_users_drafts_create) | **POST** /{userId}/drafts | 
[**gmail_users_drafts_delete**](UsersApi.md#gmail_users_drafts_delete) | **DELETE** /{userId}/drafts/{id} | 
[**gmail_users_drafts_get**](UsersApi.md#gmail_users_drafts_get) | **GET** /{userId}/drafts/{id} | 
[**gmail_users_drafts_list**](UsersApi.md#gmail_users_drafts_list) | **GET** /{userId}/drafts | 
[**gmail_users_drafts_send**](UsersApi.md#gmail_users_drafts_send) | **POST** /{userId}/drafts/send | 
[**gmail_users_drafts_update**](UsersApi.md#gmail_users_drafts_update) | **PUT** /{userId}/drafts/{id} | 
[**gmail_users_get_profile**](UsersApi.md#gmail_users_get_profile) | **GET** /{userId}/profile | 
[**gmail_users_history_list**](UsersApi.md#gmail_users_history_list) | **GET** /{userId}/history | 
[**gmail_users_labels_create**](UsersApi.md#gmail_users_labels_create) | **POST** /{userId}/labels | 
[**gmail_users_labels_delete**](UsersApi.md#gmail_users_labels_delete) | **DELETE** /{userId}/labels/{id} | 
[**gmail_users_labels_get**](UsersApi.md#gmail_users_labels_get) | **GET** /{userId}/labels/{id} | 
[**gmail_users_labels_list**](UsersApi.md#gmail_users_labels_list) | **GET** /{userId}/labels | 
[**gmail_users_labels_patch**](UsersApi.md#gmail_users_labels_patch) | **PATCH** /{userId}/labels/{id} | 
[**gmail_users_labels_update**](UsersApi.md#gmail_users_labels_update) | **PUT** /{userId}/labels/{id} | 
[**gmail_users_messages_attachments_get**](UsersApi.md#gmail_users_messages_attachments_get) | **GET** /{userId}/messages/{messageId}/attachments/{id} | 
[**gmail_users_messages_batch_delete**](UsersApi.md#gmail_users_messages_batch_delete) | **POST** /{userId}/messages/batchDelete | 
[**gmail_users_messages_batch_modify**](UsersApi.md#gmail_users_messages_batch_modify) | **POST** /{userId}/messages/batchModify | 
[**gmail_users_messages_delete**](UsersApi.md#gmail_users_messages_delete) | **DELETE** /{userId}/messages/{id} | 
[**gmail_users_messages_get**](UsersApi.md#gmail_users_messages_get) | **GET** /{userId}/messages/{id} | 
[**gmail_users_messages_import**](UsersApi.md#gmail_users_messages_import) | **POST** /{userId}/messages/import | 
[**gmail_users_messages_insert**](UsersApi.md#gmail_users_messages_insert) | **POST** /{userId}/messages | 
[**gmail_users_messages_list**](UsersApi.md#gmail_users_messages_list) | **GET** /{userId}/messages | 
[**gmail_users_messages_modify**](UsersApi.md#gmail_users_messages_modify) | **POST** /{userId}/messages/{id}/modify | 
[**gmail_users_messages_send**](UsersApi.md#gmail_users_messages_send) | **POST** /{userId}/messages/send | 
[**gmail_users_messages_trash**](UsersApi.md#gmail_users_messages_trash) | **POST** /{userId}/messages/{id}/trash | 
[**gmail_users_messages_untrash**](UsersApi.md#gmail_users_messages_untrash) | **POST** /{userId}/messages/{id}/untrash | 
[**gmail_users_settings_filters_create**](UsersApi.md#gmail_users_settings_filters_create) | **POST** /{userId}/settings/filters | 
[**gmail_users_settings_filters_delete**](UsersApi.md#gmail_users_settings_filters_delete) | **DELETE** /{userId}/settings/filters/{id} | 
[**gmail_users_settings_filters_get**](UsersApi.md#gmail_users_settings_filters_get) | **GET** /{userId}/settings/filters/{id} | 
[**gmail_users_settings_filters_list**](UsersApi.md#gmail_users_settings_filters_list) | **GET** /{userId}/settings/filters | 
[**gmail_users_settings_forwarding_addresses_create**](UsersApi.md#gmail_users_settings_forwarding_addresses_create) | **POST** /{userId}/settings/forwardingAddresses | 
[**gmail_users_settings_forwarding_addresses_delete**](UsersApi.md#gmail_users_settings_forwarding_addresses_delete) | **DELETE** /{userId}/settings/forwardingAddresses/{forwardingEmail} | 
[**gmail_users_settings_forwarding_addresses_get**](UsersApi.md#gmail_users_settings_forwarding_addresses_get) | **GET** /{userId}/settings/forwardingAddresses/{forwardingEmail} | 
[**gmail_users_settings_forwarding_addresses_list**](UsersApi.md#gmail_users_settings_forwarding_addresses_list) | **GET** /{userId}/settings/forwardingAddresses | 
[**gmail_users_settings_get_auto_forwarding**](UsersApi.md#gmail_users_settings_get_auto_forwarding) | **GET** /{userId}/settings/autoForwarding | 
[**gmail_users_settings_get_imap**](UsersApi.md#gmail_users_settings_get_imap) | **GET** /{userId}/settings/imap | 
[**gmail_users_settings_get_pop**](UsersApi.md#gmail_users_settings_get_pop) | **GET** /{userId}/settings/pop | 
[**gmail_users_settings_get_vacation**](UsersApi.md#gmail_users_settings_get_vacation) | **GET** /{userId}/settings/vacation | 
[**gmail_users_settings_send_as_create**](UsersApi.md#gmail_users_settings_send_as_create) | **POST** /{userId}/settings/sendAs | 
[**gmail_users_settings_send_as_delete**](UsersApi.md#gmail_users_settings_send_as_delete) | **DELETE** /{userId}/settings/sendAs/{sendAsEmail} | 
[**gmail_users_settings_send_as_get**](UsersApi.md#gmail_users_settings_send_as_get) | **GET** /{userId}/settings/sendAs/{sendAsEmail} | 
[**gmail_users_settings_send_as_list**](UsersApi.md#gmail_users_settings_send_as_list) | **GET** /{userId}/settings/sendAs | 
[**gmail_users_settings_send_as_patch**](UsersApi.md#gmail_users_settings_send_as_patch) | **PATCH** /{userId}/settings/sendAs/{sendAsEmail} | 
[**gmail_users_settings_send_as_smime_info_delete**](UsersApi.md#gmail_users_settings_send_as_smime_info_delete) | **DELETE** /{userId}/settings/sendAs/{sendAsEmail}/smimeInfo/{id} | 
[**gmail_users_settings_send_as_smime_info_get**](UsersApi.md#gmail_users_settings_send_as_smime_info_get) | **GET** /{userId}/settings/sendAs/{sendAsEmail}/smimeInfo/{id} | 
[**gmail_users_settings_send_as_smime_info_insert**](UsersApi.md#gmail_users_settings_send_as_smime_info_insert) | **POST** /{userId}/settings/sendAs/{sendAsEmail}/smimeInfo | 
[**gmail_users_settings_send_as_smime_info_list**](UsersApi.md#gmail_users_settings_send_as_smime_info_list) | **GET** /{userId}/settings/sendAs/{sendAsEmail}/smimeInfo | 
[**gmail_users_settings_send_as_smime_info_set_default**](UsersApi.md#gmail_users_settings_send_as_smime_info_set_default) | **POST** /{userId}/settings/sendAs/{sendAsEmail}/smimeInfo/{id}/setDefault | 
[**gmail_users_settings_send_as_update**](UsersApi.md#gmail_users_settings_send_as_update) | **PUT** /{userId}/settings/sendAs/{sendAsEmail} | 
[**gmail_users_settings_send_as_verify**](UsersApi.md#gmail_users_settings_send_as_verify) | **POST** /{userId}/settings/sendAs/{sendAsEmail}/verify | 
[**gmail_users_settings_update_auto_forwarding**](UsersApi.md#gmail_users_settings_update_auto_forwarding) | **PUT** /{userId}/settings/autoForwarding | 
[**gmail_users_settings_update_imap**](UsersApi.md#gmail_users_settings_update_imap) | **PUT** /{userId}/settings/imap | 
[**gmail_users_settings_update_pop**](UsersApi.md#gmail_users_settings_update_pop) | **PUT** /{userId}/settings/pop | 
[**gmail_users_settings_update_vacation**](UsersApi.md#gmail_users_settings_update_vacation) | **PUT** /{userId}/settings/vacation | 
[**gmail_users_stop**](UsersApi.md#gmail_users_stop) | **POST** /{userId}/stop | 
[**gmail_users_threads_delete**](UsersApi.md#gmail_users_threads_delete) | **DELETE** /{userId}/threads/{id} | 
[**gmail_users_threads_get**](UsersApi.md#gmail_users_threads_get) | **GET** /{userId}/threads/{id} | 
[**gmail_users_threads_list**](UsersApi.md#gmail_users_threads_list) | **GET** /{userId}/threads | 
[**gmail_users_threads_modify**](UsersApi.md#gmail_users_threads_modify) | **POST** /{userId}/threads/{id}/modify | 
[**gmail_users_threads_trash**](UsersApi.md#gmail_users_threads_trash) | **POST** /{userId}/threads/{id}/trash | 
[**gmail_users_threads_untrash**](UsersApi.md#gmail_users_threads_untrash) | **POST** /{userId}/threads/{id}/untrash | 
[**gmail_users_watch**](UsersApi.md#gmail_users_watch) | **POST** /{userId}/watch | 


# **gmail_users_drafts_create**
> Draft gmail_users_drafts_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Creates a new draft with the DRAFT label.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.Draft() # Draft |  (optional)

try: 
    api_response = api_instance.gmail_users_drafts_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_drafts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**Draft**](Draft.md)|  | [optional] 

### Return type

[**Draft**](Draft.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: message/rfc822
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_drafts_delete**
> gmail_users_drafts_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Immediately and permanently deletes the specified draft. Does not simply trash it.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the draft to delete.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_drafts_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_drafts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the draft to delete. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_drafts_get**
> Draft gmail_users_drafts_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, format=format)



Gets the specified draft.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the draft to retrieve.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
format = 'full' # str | The format to return the draft in. (optional) (default to full)

try: 
    api_response = api_instance.gmail_users_drafts_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_drafts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the draft to retrieve. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **format** | **str**| The format to return the draft in. | [optional] [default to full]

### Return type

[**Draft**](Draft.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_drafts_list**
> ListDraftsResponse gmail_users_drafts_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, include_spam_trash=include_spam_trash, max_results=max_results, page_token=page_token, q=q)



Lists the drafts in the user's mailbox.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
include_spam_trash = false # bool | Include drafts from SPAM and TRASH in the results. (optional) (default to false)
max_results = 100 # int | Maximum number of drafts to return. (optional) (default to 100)
page_token = 'page_token_example' # str | Page token to retrieve a specific page of results in the list. (optional)
q = 'q_example' # str | Only return draft messages matching the specified query. Supports the same query format as the Gmail search box. For example, \"from:someuser@example.com rfc822msgid: is:unread\". (optional)

try: 
    api_response = api_instance.gmail_users_drafts_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, include_spam_trash=include_spam_trash, max_results=max_results, page_token=page_token, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_drafts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **include_spam_trash** | **bool**| Include drafts from SPAM and TRASH in the results. | [optional] [default to false]
 **max_results** | **int**| Maximum number of drafts to return. | [optional] [default to 100]
 **page_token** | **str**| Page token to retrieve a specific page of results in the list. | [optional] 
 **q** | **str**| Only return draft messages matching the specified query. Supports the same query format as the Gmail search box. For example, \&quot;from:someuser@example.com rfc822msgid: is:unread\&quot;. | [optional] 

### Return type

[**ListDraftsResponse**](ListDraftsResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_drafts_send**
> Message gmail_users_drafts_send(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.Draft() # Draft |  (optional)

try: 
    api_response = api_instance.gmail_users_drafts_send(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_drafts_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**Draft**](Draft.md)|  | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: message/rfc822
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_drafts_update**
> Draft gmail_users_drafts_update(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Replaces a draft's content.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the draft to update.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.Draft() # Draft |  (optional)

try: 
    api_response = api_instance.gmail_users_drafts_update(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_drafts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the draft to update. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**Draft**](Draft.md)|  | [optional] 

### Return type

[**Draft**](Draft.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: message/rfc822
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_get_profile**
> Profile gmail_users_get_profile(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets the current user's Gmail profile.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_get_profile(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_get_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_history_list**
> ListHistoryResponse gmail_users_history_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, history_types=history_types, label_id=label_id, max_results=max_results, page_token=page_token, start_history_id=start_history_id)



Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
history_types = ['history_types_example'] # list[str] | History types to be returned by the function (optional)
label_id = 'label_id_example' # str | Only return messages with a label matching the ID. (optional)
max_results = 100 # int | The maximum number of history records to return. (optional) (default to 100)
page_token = 'page_token_example' # str | Page token to retrieve a specific page of results in the list. (optional)
start_history_id = 'start_history_id_example' # str | Required. Returns history records after the specified startHistoryId. The supplied startHistoryId should be obtained from the historyId of a message, thread, or previous list response. History IDs increase chronologically but are not contiguous with random gaps in between valid IDs. Supplying an invalid or out of date startHistoryId typically returns an HTTP 404 error code. A historyId is typically valid for at least a week, but in some rare circumstances may be valid for only a few hours. If you receive an HTTP 404 error response, your application should perform a full sync. If you receive no nextPageToken in the response, there are no updates to retrieve and you can store the returned historyId for a future request. (optional)

try: 
    api_response = api_instance.gmail_users_history_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, history_types=history_types, label_id=label_id, max_results=max_results, page_token=page_token, start_history_id=start_history_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_history_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **history_types** | [**list[str]**](str.md)| History types to be returned by the function | [optional] 
 **label_id** | **str**| Only return messages with a label matching the ID. | [optional] 
 **max_results** | **int**| The maximum number of history records to return. | [optional] [default to 100]
 **page_token** | **str**| Page token to retrieve a specific page of results in the list. | [optional] 
 **start_history_id** | **str**| Required. Returns history records after the specified startHistoryId. The supplied startHistoryId should be obtained from the historyId of a message, thread, or previous list response. History IDs increase chronologically but are not contiguous with random gaps in between valid IDs. Supplying an invalid or out of date startHistoryId typically returns an HTTP 404 error code. A historyId is typically valid for at least a week, but in some rare circumstances may be valid for only a few hours. If you receive an HTTP 404 error response, your application should perform a full sync. If you receive no nextPageToken in the response, there are no updates to retrieve and you can store the returned historyId for a future request. | [optional] 

### Return type

[**ListHistoryResponse**](ListHistoryResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_labels_create**
> Label gmail_users_labels_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Creates a new label.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.Label() # Label |  (optional)

try: 
    api_response = api_instance.gmail_users_labels_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_labels_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**Label**](Label.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_labels_delete**
> gmail_users_labels_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the label to delete.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_labels_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_labels_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the label to delete. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_labels_get**
> Label gmail_users_labels_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets the specified label.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the label to retrieve.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_labels_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the label to retrieve. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_labels_list**
> ListLabelsResponse gmail_users_labels_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Lists all labels in the user's mailbox.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_labels_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_labels_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**ListLabelsResponse**](ListLabelsResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_labels_patch**
> Label gmail_users_labels_patch(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Updates the specified label. This method supports patch semantics.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the label to update.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.Label() # Label |  (optional)

try: 
    api_response = api_instance.gmail_users_labels_patch(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_labels_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the label to update. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**Label**](Label.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_labels_update**
> Label gmail_users_labels_update(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Updates the specified label.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the label to update.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.Label() # Label |  (optional)

try: 
    api_response = api_instance.gmail_users_labels_update(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_labels_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the label to update. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**Label**](Label.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_attachments_get**
> MessagePartBody gmail_users_messages_attachments_get(user_id, message_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets the specified message attachment.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
message_id = 'message_id_example' # str | The ID of the message containing the attachment.
id = 'id_example' # str | The ID of the attachment.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_messages_attachments_get(user_id, message_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **message_id** | **str**| The ID of the message containing the attachment. | 
 **id** | **str**| The ID of the attachment. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**MessagePartBody**](MessagePartBody.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_batch_delete**
> gmail_users_messages_batch_delete(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.BatchDeleteMessagesRequest() # BatchDeleteMessagesRequest |  (optional)

try: 
    api_instance.gmail_users_messages_batch_delete(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_batch_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**BatchDeleteMessagesRequest**](BatchDeleteMessagesRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_batch_modify**
> gmail_users_messages_batch_modify(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Modifies the labels on the specified messages.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.BatchModifyMessagesRequest() # BatchModifyMessagesRequest |  (optional)

try: 
    api_instance.gmail_users_messages_batch_modify(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_batch_modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**BatchModifyMessagesRequest**](BatchModifyMessagesRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_delete**
> gmail_users_messages_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer messages.trash instead.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the message to delete.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_messages_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the message to delete. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_get**
> Message gmail_users_messages_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, format=format, metadata_headers=metadata_headers)



Gets the specified message.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the message to retrieve.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
format = 'full' # str | The format to return the message in. (optional) (default to full)
metadata_headers = ['metadata_headers_example'] # list[str] | When given and format is METADATA, only include headers specified. (optional)

try: 
    api_response = api_instance.gmail_users_messages_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, format=format, metadata_headers=metadata_headers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the message to retrieve. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **format** | **str**| The format to return the message in. | [optional] [default to full]
 **metadata_headers** | [**list[str]**](str.md)| When given and format is METADATA, only include headers specified. | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_import**
> Message gmail_users_messages_import(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, deleted=deleted, internal_date_source=internal_date_source, never_mark_spam=never_mark_spam, process_for_calendar=process_for_calendar, body=body)



Imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. Does not send a message.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
deleted = false # bool | Mark the email as permanently deleted (not TRASH) and only visible in Google Vault to a Vault administrator. Only used for G Suite accounts. (optional) (default to false)
internal_date_source = 'dateHeader' # str | Source for Gmail's internal date of the message. (optional) (default to dateHeader)
never_mark_spam = false # bool | Ignore the Gmail spam classifier decision and never mark this email as SPAM in the mailbox. (optional) (default to false)
process_for_calendar = false # bool | Process calendar invites in the email and add any extracted meetings to the Google Calendar for this user. (optional) (default to false)
body = gmail_client.Message() # Message |  (optional)

try: 
    api_response = api_instance.gmail_users_messages_import(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, deleted=deleted, internal_date_source=internal_date_source, never_mark_spam=never_mark_spam, process_for_calendar=process_for_calendar, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **deleted** | **bool**| Mark the email as permanently deleted (not TRASH) and only visible in Google Vault to a Vault administrator. Only used for G Suite accounts. | [optional] [default to false]
 **internal_date_source** | **str**| Source for Gmail&#39;s internal date of the message. | [optional] [default to dateHeader]
 **never_mark_spam** | **bool**| Ignore the Gmail spam classifier decision and never mark this email as SPAM in the mailbox. | [optional] [default to false]
 **process_for_calendar** | **bool**| Process calendar invites in the email and add any extracted meetings to the Google Calendar for this user. | [optional] [default to false]
 **body** | [**Message**](Message.md)|  | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: message/rfc822
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_insert**
> Message gmail_users_messages_insert(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, deleted=deleted, internal_date_source=internal_date_source, body=body)



Directly inserts a message into only this user's mailbox similar to IMAP APPEND, bypassing most scanning and classification. Does not send a message.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
deleted = false # bool | Mark the email as permanently deleted (not TRASH) and only visible in Google Vault to a Vault administrator. Only used for G Suite accounts. (optional) (default to false)
internal_date_source = 'receivedTime' # str | Source for Gmail's internal date of the message. (optional) (default to receivedTime)
body = gmail_client.Message() # Message |  (optional)

try: 
    api_response = api_instance.gmail_users_messages_insert(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, deleted=deleted, internal_date_source=internal_date_source, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_insert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **deleted** | **bool**| Mark the email as permanently deleted (not TRASH) and only visible in Google Vault to a Vault administrator. Only used for G Suite accounts. | [optional] [default to false]
 **internal_date_source** | **str**| Source for Gmail&#39;s internal date of the message. | [optional] [default to receivedTime]
 **body** | [**Message**](Message.md)|  | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: message/rfc822
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_list**
> ListMessagesResponse gmail_users_messages_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, include_spam_trash=include_spam_trash, label_ids=label_ids, max_results=max_results, page_token=page_token, q=q)



Lists the messages in the user's mailbox.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
include_spam_trash = false # bool | Include messages from SPAM and TRASH in the results. (optional) (default to false)
label_ids = ['label_ids_example'] # list[str] | Only return messages with labels that match all of the specified label IDs. (optional)
max_results = 100 # int | Maximum number of messages to return. (optional) (default to 100)
page_token = 'page_token_example' # str | Page token to retrieve a specific page of results in the list. (optional)
q = 'q_example' # str | Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, \"from:someuser@example.com rfc822msgid: is:unread\". Parameter cannot be used when accessing the api using the gmail.metadata scope. (optional)

try: 
    api_response = api_instance.gmail_users_messages_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, include_spam_trash=include_spam_trash, label_ids=label_ids, max_results=max_results, page_token=page_token, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **include_spam_trash** | **bool**| Include messages from SPAM and TRASH in the results. | [optional] [default to false]
 **label_ids** | [**list[str]**](str.md)| Only return messages with labels that match all of the specified label IDs. | [optional] 
 **max_results** | **int**| Maximum number of messages to return. | [optional] [default to 100]
 **page_token** | **str**| Page token to retrieve a specific page of results in the list. | [optional] 
 **q** | **str**| Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, \&quot;from:someuser@example.com rfc822msgid: is:unread\&quot;. Parameter cannot be used when accessing the api using the gmail.metadata scope. | [optional] 

### Return type

[**ListMessagesResponse**](ListMessagesResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_modify**
> Message gmail_users_messages_modify(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Modifies the labels on the specified message.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the message to modify.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.ModifyMessageRequest() # ModifyMessageRequest |  (optional)

try: 
    api_response = api_instance.gmail_users_messages_modify(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the message to modify. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**ModifyMessageRequest**](ModifyMessageRequest.md)|  | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_send**
> Message gmail_users_messages_send(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Sends the specified message to the recipients in the To, Cc, and Bcc headers.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.Message() # Message |  (optional)

try: 
    api_response = api_instance.gmail_users_messages_send(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**Message**](Message.md)|  | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: message/rfc822
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_trash**
> Message gmail_users_messages_trash(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Moves the specified message to the trash.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the message to Trash.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_messages_trash(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the message to Trash. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_messages_untrash**
> Message gmail_users_messages_untrash(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Removes the specified message from the trash.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the message to remove from Trash.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_messages_untrash(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_messages_untrash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the message to remove from Trash. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_filters_create**
> Filter gmail_users_settings_filters_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Creates a filter.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.Filter() # Filter |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_filters_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_filters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**Filter**](Filter.md)|  | [optional] 

### Return type

[**Filter**](Filter.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_filters_delete**
> gmail_users_settings_filters_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Deletes a filter.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the filter to be deleted.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_settings_filters_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_filters_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the filter to be deleted. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_filters_get**
> Filter gmail_users_settings_filters_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets a filter.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the filter to be fetched.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_filters_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_filters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the filter to be fetched. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**Filter**](Filter.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_filters_list**
> ListFiltersResponse gmail_users_settings_filters_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Lists the message filters of a Gmail user.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_filters_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_filters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**ListFiltersResponse**](ListFiltersResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_forwarding_addresses_create**
> ForwardingAddress gmail_users_settings_forwarding_addresses_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Creates a forwarding address. If ownership verification is required, a message will be sent to the recipient and the resource's verification status will be set to pending; otherwise, the resource will be created with verification status set to accepted.  This method is only available to service account clients that have been delegated domain-wide authority.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.ForwardingAddress() # ForwardingAddress |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_forwarding_addresses_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_forwarding_addresses_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**ForwardingAddress**](ForwardingAddress.md)|  | [optional] 

### Return type

[**ForwardingAddress**](ForwardingAddress.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_forwarding_addresses_delete**
> gmail_users_settings_forwarding_addresses_delete(user_id, forwarding_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Deletes the specified forwarding address and revokes any verification that may have been required.  This method is only available to service account clients that have been delegated domain-wide authority.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
forwarding_email = 'forwarding_email_example' # str | The forwarding address to be deleted.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_settings_forwarding_addresses_delete(user_id, forwarding_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_forwarding_addresses_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **forwarding_email** | **str**| The forwarding address to be deleted. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_forwarding_addresses_get**
> ForwardingAddress gmail_users_settings_forwarding_addresses_get(user_id, forwarding_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets the specified forwarding address.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
forwarding_email = 'forwarding_email_example' # str | The forwarding address to be retrieved.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_forwarding_addresses_get(user_id, forwarding_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_forwarding_addresses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **forwarding_email** | **str**| The forwarding address to be retrieved. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**ForwardingAddress**](ForwardingAddress.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_forwarding_addresses_list**
> ListForwardingAddressesResponse gmail_users_settings_forwarding_addresses_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Lists the forwarding addresses for the specified account.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_forwarding_addresses_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_forwarding_addresses_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**ListForwardingAddressesResponse**](ListForwardingAddressesResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_get_auto_forwarding**
> AutoForwarding gmail_users_settings_get_auto_forwarding(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets the auto-forwarding setting for the specified account.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_get_auto_forwarding(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_get_auto_forwarding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**AutoForwarding**](AutoForwarding.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_get_imap**
> ImapSettings gmail_users_settings_get_imap(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets IMAP settings.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_get_imap(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_get_imap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**ImapSettings**](ImapSettings.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_get_pop**
> PopSettings gmail_users_settings_get_pop(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets POP settings.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_get_pop(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_get_pop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**PopSettings**](PopSettings.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_get_vacation**
> VacationSettings gmail_users_settings_get_vacation(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets vacation responder settings.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_get_vacation(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_get_vacation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**VacationSettings**](VacationSettings.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_create**
> SendAs gmail_users_settings_send_as_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Creates a custom \"from\" send-as alias. If an SMTP MSA is specified, Gmail will attempt to connect to the SMTP service to validate the configuration before creating the alias. If ownership verification is required for the alias, a message will be sent to the email address and the resource's verification status will be set to pending; otherwise, the resource will be created with verification status set to accepted. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.  This method is only available to service account clients that have been delegated domain-wide authority.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.SendAs() # SendAs |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_send_as_create(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**SendAs**](SendAs.md)|  | [optional] 

### Return type

[**SendAs**](SendAs.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_delete**
> gmail_users_settings_send_as_delete(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Deletes the specified send-as alias. Revokes any verification that may have been required for using it.  This method is only available to service account clients that have been delegated domain-wide authority.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The send-as alias to be deleted.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_settings_send_as_delete(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The send-as alias to be deleted. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_get**
> SendAs gmail_users_settings_send_as_get(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets the specified send-as alias. Fails with an HTTP 404 error if the specified address is not a member of the collection.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The send-as alias to be retrieved.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_send_as_get(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The send-as alias to be retrieved. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**SendAs**](SendAs.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_list**
> ListSendAsResponse gmail_users_settings_send_as_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Lists the send-as aliases for the specified account. The result includes the primary send-as address associated with the account as well as any custom \"from\" aliases.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_send_as_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**ListSendAsResponse**](ListSendAsResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_patch**
> SendAs gmail_users_settings_send_as_patch(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.  Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority. This method supports patch semantics.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The send-as alias to be updated.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.SendAs() # SendAs |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_send_as_patch(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The send-as alias to be updated. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**SendAs**](SendAs.md)|  | [optional] 

### Return type

[**SendAs**](SendAs.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_smime_info_delete**
> gmail_users_settings_send_as_smime_info_delete(user_id, send_as_email, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Deletes the specified S/MIME config for the specified send-as alias.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The email address that appears in the \"From:\" header for mail sent using this alias.
id = 'id_example' # str | The immutable ID for the SmimeInfo.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_settings_send_as_smime_info_delete(user_id, send_as_email, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_smime_info_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The email address that appears in the \&quot;From:\&quot; header for mail sent using this alias. | 
 **id** | **str**| The immutable ID for the SmimeInfo. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_smime_info_get**
> SmimeInfo gmail_users_settings_send_as_smime_info_get(user_id, send_as_email, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Gets the specified S/MIME config for the specified send-as alias.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The email address that appears in the \"From:\" header for mail sent using this alias.
id = 'id_example' # str | The immutable ID for the SmimeInfo.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_send_as_smime_info_get(user_id, send_as_email, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_smime_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The email address that appears in the \&quot;From:\&quot; header for mail sent using this alias. | 
 **id** | **str**| The immutable ID for the SmimeInfo. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**SmimeInfo**](SmimeInfo.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_smime_info_insert**
> SmimeInfo gmail_users_settings_send_as_smime_info_insert(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Insert (upload) the given S/MIME config for the specified send-as alias. Note that pkcs12 format is required for the key.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The email address that appears in the \"From:\" header for mail sent using this alias.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.SmimeInfo() # SmimeInfo |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_send_as_smime_info_insert(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_smime_info_insert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The email address that appears in the \&quot;From:\&quot; header for mail sent using this alias. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**SmimeInfo**](SmimeInfo.md)|  | [optional] 

### Return type

[**SmimeInfo**](SmimeInfo.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_smime_info_list**
> ListSmimeInfoResponse gmail_users_settings_send_as_smime_info_list(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Lists S/MIME configs for the specified send-as alias.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The email address that appears in the \"From:\" header for mail sent using this alias.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_settings_send_as_smime_info_list(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_smime_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The email address that appears in the \&quot;From:\&quot; header for mail sent using this alias. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**ListSmimeInfoResponse**](ListSmimeInfoResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_smime_info_set_default**
> gmail_users_settings_send_as_smime_info_set_default(user_id, send_as_email, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Sets the default S/MIME config for the specified send-as alias.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The email address that appears in the \"From:\" header for mail sent using this alias.
id = 'id_example' # str | The immutable ID for the SmimeInfo.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_settings_send_as_smime_info_set_default(user_id, send_as_email, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_smime_info_set_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The email address that appears in the \&quot;From:\&quot; header for mail sent using this alias. | 
 **id** | **str**| The immutable ID for the SmimeInfo. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_update**
> SendAs gmail_users_settings_send_as_update(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.  Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The send-as alias to be updated.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.SendAs() # SendAs |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_send_as_update(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The send-as alias to be updated. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**SendAs**](SendAs.md)|  | [optional] 

### Return type

[**SendAs**](SendAs.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_send_as_verify**
> gmail_users_settings_send_as_verify(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Sends a verification email to the specified send-as alias address. The verification status must be pending.  This method is only available to service account clients that have been delegated domain-wide authority.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
send_as_email = 'send_as_email_example' # str | The send-as alias to be verified.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_settings_send_as_verify(user_id, send_as_email, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_send_as_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **send_as_email** | **str**| The send-as alias to be verified. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_update_auto_forwarding**
> AutoForwarding gmail_users_settings_update_auto_forwarding(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Updates the auto-forwarding setting for the specified account. A verified forwarding address must be specified when auto-forwarding is enabled.  This method is only available to service account clients that have been delegated domain-wide authority.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.AutoForwarding() # AutoForwarding |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_update_auto_forwarding(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_update_auto_forwarding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**AutoForwarding**](AutoForwarding.md)|  | [optional] 

### Return type

[**AutoForwarding**](AutoForwarding.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_update_imap**
> ImapSettings gmail_users_settings_update_imap(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Updates IMAP settings.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.ImapSettings() # ImapSettings |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_update_imap(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_update_imap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**ImapSettings**](ImapSettings.md)|  | [optional] 

### Return type

[**ImapSettings**](ImapSettings.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_update_pop**
> PopSettings gmail_users_settings_update_pop(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Updates POP settings.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.PopSettings() # PopSettings |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_update_pop(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_update_pop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**PopSettings**](PopSettings.md)|  | [optional] 

### Return type

[**PopSettings**](PopSettings.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_settings_update_vacation**
> VacationSettings gmail_users_settings_update_vacation(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Updates vacation responder settings.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | User's email address. The special value \"me\" can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.VacationSettings() # VacationSettings |  (optional)

try: 
    api_response = api_instance.gmail_users_settings_update_vacation(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_settings_update_vacation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s email address. The special value \&quot;me\&quot; can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**VacationSettings**](VacationSettings.md)|  | [optional] 

### Return type

[**VacationSettings**](VacationSettings.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_stop**
> gmail_users_stop(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Stop receiving push notifications for the given user mailbox.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_stop(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_threads_delete**
> gmail_users_threads_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Immediately and permanently deletes the specified thread. This operation cannot be undone. Prefer threads.trash instead.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | ID of the Thread to delete.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_instance.gmail_users_threads_delete(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_threads_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| ID of the Thread to delete. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

void (empty response body)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_threads_get**
> Thread gmail_users_threads_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, format=format, metadata_headers=metadata_headers)



Gets the specified thread.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the thread to retrieve.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
format = 'full' # str | The format to return the messages in. (optional) (default to full)
metadata_headers = ['metadata_headers_example'] # list[str] | When given and format is METADATA, only include headers specified. (optional)

try: 
    api_response = api_instance.gmail_users_threads_get(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, format=format, metadata_headers=metadata_headers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_threads_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the thread to retrieve. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **format** | **str**| The format to return the messages in. | [optional] [default to full]
 **metadata_headers** | [**list[str]**](str.md)| When given and format is METADATA, only include headers specified. | [optional] 

### Return type

[**Thread**](Thread.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_threads_list**
> ListThreadsResponse gmail_users_threads_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, include_spam_trash=include_spam_trash, label_ids=label_ids, max_results=max_results, page_token=page_token, q=q)



Lists the threads in the user's mailbox.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
include_spam_trash = false # bool | Include threads from SPAM and TRASH in the results. (optional) (default to false)
label_ids = ['label_ids_example'] # list[str] | Only return threads with labels that match all of the specified label IDs. (optional)
max_results = 100 # int | Maximum number of threads to return. (optional) (default to 100)
page_token = 'page_token_example' # str | Page token to retrieve a specific page of results in the list. (optional)
q = 'q_example' # str | Only return threads matching the specified query. Supports the same query format as the Gmail search box. For example, \"from:someuser@example.com rfc822msgid: is:unread\". Parameter cannot be used when accessing the api using the gmail.metadata scope. (optional)

try: 
    api_response = api_instance.gmail_users_threads_list(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, include_spam_trash=include_spam_trash, label_ids=label_ids, max_results=max_results, page_token=page_token, q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_threads_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **include_spam_trash** | **bool**| Include threads from SPAM and TRASH in the results. | [optional] [default to false]
 **label_ids** | [**list[str]**](str.md)| Only return threads with labels that match all of the specified label IDs. | [optional] 
 **max_results** | **int**| Maximum number of threads to return. | [optional] [default to 100]
 **page_token** | **str**| Page token to retrieve a specific page of results in the list. | [optional] 
 **q** | **str**| Only return threads matching the specified query. Supports the same query format as the Gmail search box. For example, \&quot;from:someuser@example.com rfc822msgid: is:unread\&quot;. Parameter cannot be used when accessing the api using the gmail.metadata scope. | [optional] 

### Return type

[**ListThreadsResponse**](ListThreadsResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_threads_modify**
> Thread gmail_users_threads_modify(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Modifies the labels applied to the thread. This applies to all messages in the thread.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the thread to modify.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.ModifyThreadRequest() # ModifyThreadRequest |  (optional)

try: 
    api_response = api_instance.gmail_users_threads_modify(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_threads_modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the thread to modify. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**ModifyThreadRequest**](ModifyThreadRequest.md)|  | [optional] 

### Return type

[**Thread**](Thread.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_threads_trash**
> Thread gmail_users_threads_trash(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Moves the specified thread to the trash.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the thread to Trash.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_threads_trash(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_threads_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the thread to Trash. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**Thread**](Thread.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_threads_untrash**
> Thread gmail_users_threads_untrash(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)



Removes the specified thread from the trash.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
id = 'id_example' # str | The ID of the thread to remove from Trash.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)

try: 
    api_response = api_instance.gmail_users_threads_untrash(user_id, id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_threads_untrash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **id** | **str**| The ID of the thread to remove from Trash. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 

### Return type

[**Thread**](Thread.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gmail_users_watch**
> WatchResponse gmail_users_watch(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)



Set up or update a push notification watch on the given user mailbox.

### Example 
```python
from __future__ import print_statement
import time
import gmail_client
from gmail_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2
gmail_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = gmail_client.UsersApi()
user_id = 'user_id_example' # str | The user's email address. The special value me can be used to indicate the authenticated user.
alt = 'json' # str | Data format for the response. (optional) (default to json)
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
key = 'key_example' # str | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. (optional)
oauth_token = 'oauth_token_example' # str | OAuth 2.0 token for the current user. (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. (optional)
user_ip = 'user_ip_example' # str | IP address of the site where the request originates. Use this if you want to enforce per-user limits. (optional)
body = gmail_client.WatchRequest() # WatchRequest |  (optional)

try: 
    api_response = api_instance.gmail_users_watch(user_id, alt=alt, fields=fields, key=key, oauth_token=oauth_token, pretty_print=pretty_print, quota_user=quota_user, user_ip=user_ip, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->gmail_users_watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user&#39;s email address. The special value me can be used to indicate the authenticated user. | 
 **alt** | **str**| Data format for the response. | [optional] [default to json]
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **str**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauth_token** | **str**| OAuth 2.0 token for the current user. | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided. | [optional] 
 **user_ip** | **str**| IP address of the site where the request originates. Use this if you want to enforce per-user limits. | [optional] 
 **body** | [**WatchRequest**](WatchRequest.md)|  | [optional] 

### Return type

[**WatchResponse**](WatchResponse.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

