# SendAs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A name that appears in the \&quot;From:\&quot; header for mail sent using this alias. For custom \&quot;from\&quot; addresses, when this is empty, Gmail will populate the \&quot;From:\&quot; header with the name that is used for the primary address associated with the account. | [optional] 
**is_default** | **bool** | Whether this address is selected as the default \&quot;From:\&quot; address in situations such as composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is true. Changing this from false to true for an address will result in this field becoming false for the other previous default address. | [optional] 
**is_primary** | **bool** | Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases. This field is read-only. | [optional] 
**reply_to_address** | **str** | An optional email address that is included in a \&quot;Reply-To:\&quot; header for mail sent using this alias. If this is empty, Gmail will not generate a \&quot;Reply-To:\&quot; header. | [optional] 
**send_as_email** | **str** | The email address that appears in the \&quot;From:\&quot; header for mail sent using this alias. This is read-only for all operations except create. | [optional] 
**signature** | **str** | An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. | [optional] 
**smtp_msa** | [**SmtpMsa**](SmtpMsa.md) | An optional SMTP service that will be used as an outbound relay for mail sent using this alias. If this is empty, outbound mail will be sent directly from Gmail&#39;s servers to the destination SMTP service. This setting only applies to custom \&quot;from\&quot; aliases. | [optional] 
**treat_as_alias** | **bool** | Whether Gmail should  treat this address as an alias for the user&#39;s primary email address. This setting only applies to custom \&quot;from\&quot; aliases. | [optional] 
**verification_status** | **str** | Indicates whether this address has been verified for use as a send-as alias. Read-only. This setting only applies to custom \&quot;from\&quot; aliases. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


