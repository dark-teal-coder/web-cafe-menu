# Solutions to Problems in Exam Prep: AWS Certified Cloud Practitioner Foundations

There are a few types of questions in the quizzes in the course. See the list of the question types below.

1. Multiple choice
2. Code
3. Value input/output

For type 1, start the solution with `- [x]`; for type 2, use triple backticks to create a Python code block; for type 3, use single backticks.

The graded assessments usually have 10 questions in them but there is a pool of over 10 questions for every graded assessment. Therefore, we get different questions every time we attempt the assessments. The following solutions may not all be the same as what you see when you do the assessments.

---

## Module 04

### 04.01 Benchmark Assessment

#### 04.01.02 Benchmark Assessment

***Solution 01***

- [x] A list of instructions that the computer has to follow to reach a goal

***Solution 02***

- [x] The rules of how to express things in that language

***Solution 03***

- [x] There’s not much difference, but scripts are usually simpler and shorter.

***Solution 04***

Multiple answers:

- [x] Generating a sales report, split by region and product type
- [x] Copying a file to all computers in a company

***Solution 05***

- [x] The intended meaning or logic of coded statements







1. The ability to horizontally scale Amazon EC2 instances based on demand is an example of which concept in the AWS Cloud value proposition? 
= Elasticity

2. What are the benefits of developing and running a new application in the AWS Cloud compared to on-premises? (Select TWO.) 
= AWS provides options to architect for high availability.
= AWS can scale resources to changing application demands.

3. AWS services can relieve a company's IT staff of which of the following IT tasks? (Select TWO.) 
= Planning the capacity for object storage
= Patching database engine on Amazon RDS DB instances

4. A user wants the ability to easily scale compute resources in and out, while only paying for the resources used. Which AWS Cloud architecture principle is this? 
= Elasticity

5. Which of the following are benefits of using the AWS Cloud? (Select TWO.) 
= Increased speed and agility
= Ability to deploy globally in minutes

6. Which on-premises expense will be reduced if the company migrates their application to Amazon EC2? 
= Server hardware costs

7. What does the AWS Simple Monthly Calculator provide? 
= Estimated costs for an AWS Cloud architecture

8. A company wants to use Amazon Elastic Compute Cloud (Amazon EC2) to deploy a global commercial application. The deployment solution should be built with the highest redundancy and fault tolerance. Based on this situation, the Amazon EC2 instances should be deployed: 
= Across multiple Availability Zones in two AWS Regions

9. Which of the following is an AWS Cloud architecture design principle? 
= Implement loose coupling.

10. Which design principles for cloud architecture are recommended when re-architecting a large monolithic application? (Select TWO.) 
= Implement loose coupling.
= Design for scalability.

11. A user wants to implement loose coupling in their application architecture. Which AWS service meets this requirement? 
= Amazon SQS

12. Which of the following is the customer's responsibility under the AWS shared responsibility model? 
= Patching the operating systems that were deployed on Amazon EC2 instances

13. Under the shared responsibility model, which of the following are responsibilities of AWS? 
= Securing physical infrastructure

14. Which service enables risk auditing by continuously monitoring and logging API requests to resources in an account, including user actions in the AWS Management Console and AWS SDKs? 
= AWS CloudTrail

15. Which of the following will enhance the security of access to the AWS Management Console? (Select TWO.) 
= Multi-factor authentication (MFA)
= Complex password policies

16. Which of the following can limit Amazon Simple Storage Service (Amazon S3) bucket access to specific users? 
= AWS Identity and Access Management (IAM) policies

17. Which of the following AWS Identity and Access Management (IAM) best practice helps protect an AWS account? 
= Use multi-factor authentication (MFA) to protect the AWS account root user. (IAM) policies

18. Which AWS service or feature can be used to prevent SQL injection attacks? 
= AWS WAF

19. Where can users find a catalog of AWS-recognized providers of third-party security solutions? 
= AWS Marketplace

20. Which components are required to build a successful site-to-site VPN connection on AWS? (Select TWO.) 
= Customer gateway
= Virtual private gateway

21. Which aspect of AWS infrastructure enables global deployment of compute and storage? 
= Regions

22. What can AWS edge locations be used for? (Select TWO.) 
= Delivering content closer to users
= Reducing the load on EC2 based web servers

23. What is a characteristic of Amazon S3 Cross-Region Replication? 
= S3 buckets configured for Cross-Region Replication can be owned by a single AWS account or by different accounts.

24. Which AWS services will support data replication across Regions? (Select TWO.) 
= Amazon S3
= Amazon Relational Database Service

25. Which AWS service can MOST efficiently import exabytes of data to the AWS Cloud from an on-premises environment? 
= AWS Snowmobile

26. Which of the following are benefits of running a database on Amazon RDS compared to an on-premises database? (Select TWO.) 
= Amazon RDS provides backups by default.
= Amazon RDS database compute capacity can be easily scaled.

27. Which AWS service runs containers without needing to provision and manage Amazon EC2 instances? 
= AWS Fargate

28. Which of the following AWS services are serverless? (Select TWO.) 
= AWS Lambda
= Amazon API Gateway

29. A user has petabytes of data to migrate to AWS from an area where high-speed network connections are not possible. Which service is the FASTEST way to transfer the data? 
= AWS Snow Family

30. Which AWS compute service is serverless? 
= AWS Lambda

31. Which AWS service helps customers collect, process, and analyze real-time streaming data from sources such as operating logs, financial transactions, and social media feeds? 
= Amazon Kinesis

32. Which of the following is an AWS database service that provides virtually unlimited throughput and scale?  
= Amazon DynamoDB

33. Which AWS service or feature allows a company to visualize, understand, and manage AWS costs and usage over time? 
= AWS Cost Explorer

34. A company is considering migrating their applications from their on-premises data centers to the AWS Cloud. How could this decision lower the company's Total Cost of Ownership (TCO) of their applications? 
= Using the AWS Cloud eliminates the need for large capital expenditures

35. A company is using the AWS CLI and programmatic access of Amazon RDS resources from its on-premises network. What is a mandatory requirement in this scenario? 
= Using an AWS access key and a secret key

36. A company is running a production workload on AWS. Which AWS Support plan will provide the company with technical support within 15 minutes of a user opening a case concerning a critical service interruption? 
= Enterprise Support

37. What technology enables compute capacity to adjust as loads change? 
= Automatic scaling

38. A user would like to encrypt data that is received, stored, and managed by AWS CloudTrail. Which AWS service will provide this capability? 
= AWS Key Management Service (AWS KMS)

39. Which of the following are features of Amazon CloudWatch Logs? (Select TWO.) 
= Real-time monitoring
= Adjustable retention

40. Which AWS Identity and Access Management (IAM) feature allows developers to access Amazon S3 through the AWS CLI? 
= Access keys

41. Which of the following services will automatically scale with an expected increase in web traffic? 
= Elastic Load Balancing

42. Which AWS Support plan provides access to architectural and operational reviews, as well as 24/7 access to senior cloud support engineers through email, online chat, and phone? 
= Enterprise Support

43. Which of the following Amazon EC2 pricing models allows customers to use existing server-bound software licenses? 
= Dedicated Hosts

44. A company has an application that only needs to run for 2 hours at any time during a day. Which Amazon EC2 instance type will be MOST cost-effective for this application? 
= Spot Instances

45. How can Amazon EC2 Reserved Instances be shared across multiple AWS accounts? 
= AWS Organizations consolidated billing

46. How can one AWS account use Reserved Instances from another AWS account? 
= By using AWS Organizations consolidated billing

47. Which tool can only be used to track AWS usage and estimated charges related to it? 
= Cost Explorer

48. A user has underutilized on-premises resources. Which AWS Cloud concept can BEST address this issue?  
= Elasticity

49. Users report latency when they connect to a website with a global customer base. Which AWS service will improve the customer experience by reducing latency? 
= Amazon CloudFront

50. Which AWS services decrease network latency for global users of an application that is hosted in the AWS Cloud? (Select TWO.) 
= Amazon CloudFront
= AWS Global Accelerator
