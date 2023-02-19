# Week 0 — Billing and Architecture

# Homework Challenges

## Logical Diagram

- [Logical diagram v1](../_docs/assets/week0/images/Cruddur%20-%20Logical%20Diagram.png)

- [Logical Lucidchart](https://lucid.app/lucidchart/49f7d1f7-ff3a-471b-8674-bd23124c4ef6/edit?viewport_loc=-414%2C-463%2C2899%2C1459%2C0_0&invitationId=inv_13e5eaeb-5cc2-426c-afbd-9f1aa4c6acb5)


## CI/CD Pipline

- [Pipline Lucidchart](https://lucid.app/lucidchart/12ffdba1-6cff-46f2-b665-1a8773b81caf/edit?beaconFlowId=5E31E2692B026FAE&invitationId=inv_62dffc7f-1b95-46b9-94c8-2b8828bdf9ec&page=0_0#)

- [Pipline v1](../_docs/assets/week0/images/Crudur%20-%20Pipline.png)
- [Pipline v2](../_docs/assets/week0/images/Crudur%20-%20Pipline-v2.png)


Three stages will be added to the pipline

- Lint
- Test
- Build
- Deploy
  
### Lint
Check and validate fprmating ...

### test
Run the unitest 

### Build
Build tha packages or docker images and push them to ECR

### Deploy 
Trigger codedeploy to deploy the new version of the application. Bleu green deployment will be configured in the code deploy to avoid breaking the production

## Use EventBridge to hookup Health Dashboard to SNS and send notification when there is a service health issue


1. Create the event bridge rule
```bash
aws  events list-rules    --profile bootcamp
```

```json
{
    "Rules": [
        {
            "Name": "AWSHealthDashboardHealthCheckRule",
            "Arn": "arn:aws:events:us-east-1:<ACCOUNT-ID>:rule/AWSHealthDashboardHealthCheckRule",
            "EventPattern": "{\"source\":[\"aws.health\"]}",
            "State": "ENABLED",
            "Description": "Rule to check the AWS health check",
            "EventBusName": "default"
        }
    ]
}
```

2. Create SNS topic

```bash
aws  sns list-topics  --profile bootcamp
```
```json
{
    "Topics": [
        {
            "TopicArn": "arn:aws:sns:us-east-1:<ACCOUNT-ID>:AWSHealthCheckTopic"
        }
    ]
}
```
3. Add target to SNS topic
```bash
aws  events list-targets-by-rule  --rule AWSHealthDashboardHealthCheckRule   --profile bootcamp
```
```json
{
    "Targets": [
        {
            "Id": "Id66b940a0-0b4a-4534-8298-12a252ef78ab",
            "Arn": "arn:aws:sns:us-east-1:<ACCOUNT-ID>:AWSHealthCheckTopic"
        }
    ]
}
```
4. Subscribe to the topic
```bash
aws  sns list-subscriptions-by-topic  --topic arn:aws:sns:us-east-1:<ACCOUNT-ID>:AWSHealthCheckTopic   --profile bootcamp
```
```json
{
    "Subscriptions": [
        {
            "SubscriptionArn": "arn:aws:sns:us-east-1:<ACCOUNT-ID>:AWSHealthCheckTopic:ceff8deb-c0b8-439c-8875-4cda5ae9ad88",
            "Owner": "<ACCOUNT-ID>",
            "Protocol": "email",
            "Endpoint": "MYEMAIL@gmail.com",
            "TopicArn": "arn:aws:sns:us-east-1:<ACCOUNT-ID>:AWSHealthCheckTopic"
        }
    ]
}
```
- [notification proof](../_docs/assets/week0/images/proof-event-bridge.png)
