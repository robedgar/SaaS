# Copykitt: SaaS Project

This is a SaaS application that generates AI branding snippets and keywords for the customer's brand.
It is a full stack application.

## **Examples**

---

Try out the demo here (requires authentication):

<img align="center" src="https://raw.githubusercontent.com/pixegami/copykitt-tutorial/main/images/copykitt_results.png" >

**Lambda Layer ZIP**

---

I've decided to actually commit the Lambda layer zip file itself along with the project since a few people have told me they have trouble building this Docker image themselves.
So you can either follow the tutorial and try to build it (it's easier on a Linux or Mac), or if it doesn't work, then just use the copykitt-infra/lambda_base_layer/layer.zip file I have provided.

**Tech Stack**

---

Backend Stack

Colons can be used to align columns.

| Type      |       Tech       |
| --------- | :--------------: |
| Language  |      Python      |
| Framework |     FastApi      |
| Hosting   | AWS(Lambda+ Api) |
