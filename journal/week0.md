# Week 0 — Billing and Architecture

# Pipline

- [Pipline Lucidchart](https://lucid.app/lucidchart/12ffdba1-6cff-46f2-b665-1a8773b81caf/edit?beaconFlowId=5E31E2692B026FAE&invitationId=inv_62dffc7f-1b95-46b9-94c8-2b8828bdf9ec&page=0_0#)

- [Pipline v1](../week0/images/Crudur%20-%20Pipline.png)
- [Pipline v2](../week0/images/Crudur%20-%20Pipline-v2.png)


Three stages will be added to the pipline

- Lint
- Test
- Build
- Deploy
  
## Lint
Check and validate fprmating ...

## test
Run the unitest 

## Build
Build tha packages or docker images and push them to ECR

## Deploy 
Trig codedeploy to deploy the new version of the application. Bleu green deployment will be configured in the code deploy to avoid breaking the production