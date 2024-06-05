# Project 3 Deliverables:

**Team Number:** 17

**Project Title:** Casino Management System (CMS)

---

## Task 1: Requirements and Subsystems

### **1.1 Functional Requirements:**

- **User Management:**
    - Register and manage customer accounts
    - Manage employee accounts and roles
    - Track user activity and gameplay data
- **Casino Management:**
    - Manage sub-brands and individual casino information
    - Track financial data (income, expenses, profits)
    - Monitor game table performance and profitability
- **Game Table Management:**
    - Configure and manage different types of game tables
    - Track game table usage and profitability
- **Chips Management:**
    - Facilitate chip purchase and redemption
- **Payment Processing:**
    - Support cash and various electronic payment methods (UPI, debit card)
- **Notifications:**
    - Send notifications to subscribed customers of a casino.

### **1.2 Non-Functional Requirements:**

- **Security:** Protect user data from unauthorized access
- **Performance:** Ensure fast response times and efficient operations
- **Flexibility:** Easily add new casino sub-brands and game types
- **Usability:** Provide a user-friendly interface for both customers and casinos

**Architecturally Significant Requirements:**

- **User Management:** Securely storing and managing user data is crucial for system security and privacy.
- **Flexibility/Extendibility:** The ability to add new casinos and game types easily impacts the design of the data model and system architecture.

### **1.3 Subsystem Overview:**

- **User Management Subsystem:** Handles user registration, authentication, and authorization. The password is stored using bcrypt for safety purpose. Admin has the power to add new managers while manager can log in and perform its functions like creating casinos etc.
- **Casino Management Subsystem:** Manages casino information, financial data, and game table performance.
    - Includes creation of a Casino using a builder pattern with the no of game tables, bars, staff given as user input if you are a manager.
    - Lists all the casinos if you are a user. We can click on a particular casino and the gametables and bars present in the casino will be displayed . User can click on any gametable and play which can lead to his/her profit or loss that will be stored in the database.
- **Game Management Subsystem:** Configures and tracks game tables and gameplay data.
- **Payment Processing Subsystem:** Handles chip purchases, redemptions, and integrates with external payment gateways.
    - The entire subsystem is built on Strategy pattern for different modes of payments including card, cash and upi.
    - Have a method to convert cash into tokens and these tokens are then used to play in the casino.
    - Implemented Adapter pattern for handling cash payment through US Dollars.
- **Notification Subsystem:** In this subsystem the user is able to subscribe to any casino that it wants to and the manager of that casino can notify these users for any new updates.
- **Analytic Subsystem:** In this subsystem, both the user and the manager can analyze the overall money they have spent and the overall profit/loss they are in.
    - **User:** The user can see the profits/losses he has made on the casinos he went to based on a particular day and in terms of usability, easily keep track of his overall expenses in different casinos.
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled.png)
    
    - **Manager**:
        - A manager can analyze all the casinos under him and see the overall profit/loss he has made (on a daily basis graphically). He can analyze which casino is making more profit and what’s the daily trend of the casinos (implying the season when he expects the most profits). He can also easily check any abnormal patterns (for instance a casino going into loss drastically or consistently) and take measures.
            
            ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%201.png)
            
        - Within every casino as well, the manager can analyze all the profits/losses made within all the game tables in that casino as well which can be used to analyze which game tables are bringing him more profits so that he can increase those particular kinds while creating a new casino.
        
        ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%202.png)
        

---

## Task 2: Architecture Framework

### **2.1 Stakeholder Identification (IEEE 42010):**

| Stakeholder | Concerns | Viewpoint/View |
| --- | --- | --- |
| Customers | Security, usability, performance | User Interface, System Performance |
| Casino Operators | Profitability, efficiency, data insights | Management Dashboards, Financial Reports |
| System Administrators | Security, reliability, maintainability | System Architecture |
| Developers | Code quality, maintainability, extensibility | System Design, Code Structure |

### **2.2 Major Design Decisions (ADRs):**

| ADR | Decision | Rationale |
| --- | --- | --- |
| 1 | Use SQL database, Python, and React | Familiar technologies, suitability for project requirements |
| 2 | Implement Layered Architecture pattern | Not a huge system, modularity, maintainability so Layered was preferred over MicroService |
| 3 | Utilize a single central database | Simplifies data management, ensures data consistency , improved data access , enhances security and compliance |
| 4 | Employ RESTful API for communication | Standardized interface, flexibility for future integrations,loose coupling between client and server,more secure ( used JWT(in our case)) |
| 5 | Choice of database | SQL over MongoDB as most of our data is relational so SQL is a better fit for relational data.The analytics can be done easily when we use SQL over MongoDb |

---

## Task 3: Architectural Tactics and Patterns

### **3.1 Architectural Tactics:**

- **Security Tactics**
    - Authenticate Users - During login we are checking the credentials of the user and using bcrypt for the password.
    - Authorize Users - Using the token saved in the localstorage we are fetching the userid and and their roles at every crucial backend calls.
    - Data Confidentiality - Password has been encrypted using bcrypt library for confidentiality.
- **Availability Tactics**
    - Exception Handling - In order to avoid a total shutdown, the system gracefully handles faults or errors that arise from backend API calls. Rather, it ensures that the system stays functional and responsive to user requests by responding with instructive error messages. This strategy improves the system's overall availability and dependability by proactively addressing possible problems, which supports continuous service delivery.
- **Modifiability Tactics**
    - Semantic Coherence - Consistently maintaining semantic coherence throughout the codebase is key to enhancing modifiability. This ensures that the code remains clear and understandable across all components, enabling developers to easily make changes or additions without complexity. By organizing code cohesively, development becomes simpler, leading to a more adaptable architecture that can efficiently evolve to meet evolving business needs.

### **3.2 Implementation Patterns:**

- **Adapter Pattern (Implemented):**
    
    We have a class Currency Converter defined which is used to convert the USD$ to Indian Rupees. The Class PaymentStrategyAdapter is the adapter class.
    

![16.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/16.png)

In the process_payment function if the payment method is cash we use the **CashPayment** as paymentcontext. If the currency used is USD$ , we wrap the adapter **PaymentStrategyAdpater** around the payment context(**CashPayment**) . When we call pay method it directs to the method pay defined in the adapter which first converts the USD dollars to Indian Rupees and then that pay function is executed which is done in INR case.

![15.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/15.png)

- **Strategy Pattern (Implemented):** To handle different payment methods flexibly.
    
    The strategy pattern was implemented between cash, card and UPI
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%203.png)
    
    In our CMS, we've seamlessly integrated a robust payment strategy system that enhances user flexibility and convenience when conducting transactions within our platform. Leveraging the versatile `Strategy Pattern`, we've crafted an adaptable architecture that empowers users to seamlessly choose their preferred payment methods while ensuring scalability and maintainability of our payment system.
    
    With this implementation, users can select from a variety of payment methods, including cash, card, and UPI, each tailored to suit their individual preferences and needs. This flexibility allows users to conduct transactions using the method that best aligns with their financial habits and requirements.
    
    Behind the scenes, when a user selects a payment method, our system dynamically applies the corresponding payment strategy to execute the transaction seamlessly. For instance, when a user opts for a card payment, our system utilizes the Card Payment Strategy, facilitating secure and efficient card-based transactions. Similarly, for UPI payments, the UPI Payment Strategy seamlessly handles the transaction process, providing users with a hassle-free experience.
    
    PaymentStrategy.py
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%204.png)
    
    PaymentContext.py
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%205.png)
    
    ConcreteStrategy.py
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%206.png)
    
    TokenWalletResource.py
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%207.png)
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%208.png)
    
    Frontend request
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%209.png)
    
    Furthermore, our payment strategy system promotes code reusability and maintainability by encapsulating payment method-specific logic within separate strategy classes. This modular approach simplifies code management and facilitates efficient testing and debugging.
    
- **Observer Pattern (Implemented):** For notification to subscribed users.
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2010.png)
    
    In our CMS, we have integrated a feature that allows users to subscribe to or unsubscribe from specific casinos. This subscription system allows users to receive updates and notifications about the casinos they are interested in. We used the `Observer Pattern` to implement this functionality
    
    When a user subscribes to a casino, they will begin to receive notifications from the casino manager. These notifications can include updates about new game tables, changes in staff, or special events and promotions. This feature enhances the user experience by keeping them connected and informed about their favorite casinos.
    
    Managers have the ability to send notifications to all subscribed users. This can be done through the manager's interface. By clicking the "Notify" button, managers can send a message to all subscribers of their casino. This feature allows managers to effectively communicate updates and important information to their casino's user base.
    
    The process of sending notifications is handled through the `/notify` API. When a manager sends a notification, the backend code retrieves a list of all users subscribed to the casino and then sends the notification to each of these users. The notification is then stored in the database and can be viewed by the user at any time on their "Notifications" page.
    
    ![call from frontend](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2011.png)
    
    call from frontend
    
    ![SubscriptionDao](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2012.png)
    
    SubscriptionDao
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2013.png)
    
    ![backend receives the call in CasinoResource.py](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2014.png)
    
    backend receives the call in CasinoResource.py
    
    ![add/remove subscribers from a casino](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2015.png)
    
    add/remove subscribers from a casino
    
    ![send notifications function in Casino class](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2016.png)
    
    send notifications function in Casino class
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2017.png)
    
    ![adds the notification to db.](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2018.png)
    
    adds the notification to db.
    
    User notifications are fetched on the `/get_user_notifications` API, which uses the get_user_notifications function of the user_dao, converts it to a notifs array, and returns to the frontend. The frontend is shown in the image above.
    
    ![Fetch all user notifications](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2019.png)
    
    Fetch all user notifications
    
    ![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2020.png)
    
    ![backend receives the request in UserResource.py ](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2021.png)
    
    backend receives the request in UserResource.py 
    
    ![User  interface for viewing notifications](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2022.png)
    
    User  interface for viewing notifications
    
- **Builder Pattern (Implemented):**
    
    We have implemented Builder Pattern for creation of casino. Below is the directory structure which is in the lines of Builder Pattern that contains a Director to control the flow of creation , an interface which is implemented by different concrete builders (they have different implementations of the same function defined in the interface).
    

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2023.png)

In the **CasinoDirector.py** implementation of different types of casinos (there are 4 types of casinos) are present which builds the casinos according to pre defined conditions.

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2024.png)

Below is the getResult function to return the casino built that is required by the user 

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2025.png)

[**CasinoBuilder.py**](http://CasinoBuilder.py) file defines the functions that should be implemented by concrete builders.(here we have only one builder but multiple builders can be made and they should inherit the common interface).

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2026.png)

**ConcreteCasinoBuilder.py** inherits the CasinoBuilder class where all the implementations of gametable, bar, tokencounter creation is present.

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2027.png)

[**CasinoResource.py](http://CasinoResource.py)** contains function add_casino which takes the request at the frontedd path ‘/casino/add’ and creates a casino using Builder [pattern.](http://pattern.It)This is done by retrieving the no of different gametables the user wants and first assigning staff members to them . A director is then made which handles the construction of the casino and finally we return the CasinoId.

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2028.png)

This returns the staffid(s)  for the number of gametables that the user wants .

![11.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/11.png)

This function is defined in **StaffDao.py** which updates the id of the staff so to assign it to a particular gametable.

![13.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/13.png)

This function is defined in [**GameTableDao.py](http://GameTableDao.py)** which inserts an entry of a gametable into the gametable Table 

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2029.png)

These functions are defined in **[CasinoDao.py](http://CasinoDao.py)** which adds a token counter and a bar into the corresponding tables.

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2030.png)

This is the flow of the creation of Casino using builder pattern

1. A frontend path is defined where we retrieve the user input.
2. We get the stafflist which doesn’t have any gametable or bar assigned to them.
3. We create a CasinoBuilder and pass it to the CasinoDirector.
4. Then we call the corresponding `constructCasino{type}()` function which is implemented in the director.
5. After this we call the `.getResult()` function to get the final built Casino class object.

## **Diagrams:**

### Layered Architectural Pattern

![100.jpeg](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/100.jpeg)

### MicroService Architectural Pattern

![101.jpeg](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/101.jpeg)

---

## Task 4: Prototype Implementation and Analysis

### **4.1 Prototype Development:**

- We developed a prototype for the CMS whose repo link has been provided at the end of the document.

### **4.2 Architecture Analysis:**

- **Layered Architecture:** Divides the system into presentation, service, data access, and persistence layers for clear separation of concerns. The directory structure for layered architectural pattern is given below:
    
    The layers present in our System are:
    
    1. Presentation: Frontend
    2. Service: Resource files
    3. Data Access: DAO files
    4. Persistence layers: Database (.db file - using SQLite3)

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2031.png)

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2032.png)

- **Microservices Architecture:** Architectural approach to build software applications as a collection of small, independent services, each focused on a specific business function and communicating via APIs.
    
    We have a middleman which is running on port 5000. Basically all the redirects  that the frontend does to the backend is directed to the functions defined in the middleman.
    
    ![21.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/21.png)
    
    This is a snippet of function defined to handle get request at the path ‘/wallet/balance’ which basically redirects it into the microservice which handles payment functionality and return the response.
    
    ![23.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/23.png)
    
    Similarly below is the function to handle the post request at the path ‘/casino/add’ which is redirected to the microservice which handles the non payment functionality.
    
    ![22.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/22.png)
    
    The other subsystem’s microservice is running on the port 5001 
    
    ![24.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/24.png)
    
    The payment microservice is running on the port 8080.
    
    ![26.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/26.png)
    
    This is the directory structure
    
    ![25.png](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/25.png)
    
    ![3.jpeg](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/3.jpeg)
    
    ![2.jpeg](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/2.jpeg)
    
    ![1.jpeg](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/1.jpeg)
    

## Comparison between layered and microservice architecture:

We used Locust for the performance comparison.

Quality Matrix used: Response Time and Throughput

### Layered Architectural Pattern

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2033.png)

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2034.png)

 We did for 100 users ramping up at 5 users/seconds.

**Observations:**

1. Average response time for /users/add and /users/login is comparatively more as compared to other API calls since we are using bcrypt to hash the password and storing it.
2. The endpoints related to casino information (/all_casinos, /casino_info) exhibit relatively low response times and stable performance.
3. The endpoints related to wallet operations (/wallet/addBalance, /wallet/update) show moderate response times, but they are relatively stable with no failed requests.

**Aggregated Performance**:

1. Overall, there were 2926 requests with no failed requests across all endpoints.
2. The median response time for all endpoints is 33 ms, while the average response time is 146.54 ms.
3. The aggregated current RPS is 60.7, indicating the total throughput of the system.

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2035.png)

### Microservice Architectural Pattern

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2036.png)

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2037.png)

1. **Response Time Statistics**:
    - The response time statistics provide insights into the distribution of response times across percentiles for each endpoint.
    - Endpoints related to user management (/users/add, /users/login) exhibit significantly higher response times compared to other endpoints, indicating potential performance issues or complexity in user-related operations.
    - Endpoints related to casino information (/all_casinos, /casino_info) and wallet operations (/wallet/addRecordBalance, /wallet/update) show relatively lower to moderate response times, suggesting efficient performance for these operations.
2. **Overall Observations**:
    - User-related endpoints show higher response times, possibly due to the complexity of the operations involved, such as user authentication and account management.
    - Endpoints related to casino information and wallet operations exhibit relatively lower to moderate response times, indicating efficient performance for these functionalities.
    - The aggregated response time statistics provide an overview of the overall performance of the application, with response times ranging from low to high across different percentiles.

![Untitled](Project%203%20Deliverables%20c8e17e3510df4e17b8e8d386f398d687/Untitled%2038.png)

- **IN-DEPTH ANALYSIS:**
    
    **Response Times Comparison**
    
    **Graphical Analysis:**
    
    1. **Microservice Architecture**:
        - The response times varied with increased user load, starting from an average response time of 154.9 ms for 65 users and escalating to 225.7 ms for 100 users.
        - The 95th percentile response times showed a marked increase from 390 ms to 990 ms as the load increased from 15 to 100 users, demonstrating how response times degrade under heavy load.
    2. **Layered Architecture**:
        - Started with a slightly higher baseline response time of 190 ms for a smaller user set and increased to 240 ms for the full load.
        - The 95th percentile response times were consistently lower than those in the microservice setup, starting at 410 ms and increasing to 800 ms, indicating a less sharp rise under stress.
    
    **Analysis**:
    
    - The microservice architecture exhibits a faster response under lower loads but deteriorates more significantly under high traffic, which could indicate network latency or service bottlenecks.
    - The layered architecture maintains more consistent response times, potentially due to a more predictable in-process communication setup that avoids network delays.
    
    ### Throughput Metrics
    
    **Graphical Analysis:**
    
    1. **Microservice Architecture**:
        - Throughput showed an impressive increase with initial user load, peaking early before plateauing as the system became saturated.
    2. **Layered Architecture**:
        - Exhibited a gradual throughput increase, which did not peak as sharply but maintained a steady increment pace throughout the test.
    
    **Analysis**:
    
    - The microservice architecture can handle a high number of transactions up to a point, beyond which it stabilizes, possibly due to reaching service limits or network constraints.
    - The layered architecture ramps up more evenly, possibly reflecting a limit in resource allocation that spreads more evenly across the system components.
    
1. **Complexity:**
    - Layered Architecture: Has fewer components and a simpler structure, making it easier to understand and manage.
    - Microservices Architecture: Higher complexity due to the distributed nature of services, network communication overhead, and the need for additional infrastructure for service discovery, monitoring, and management.
2. **Scalability:**
    - Layered Architecture: Scaling is more challenging as the entire application is typically scaled together, limiting the ability to independently scale individual components.
    - Microservices Architecture: Better scalability as individual services can be scaled independently based on demand, allowing for more efficient resource utilization and horizontal scaling.
3. **Maintainability:**
    - Layered Architecture: Changes and updates may be easier to implement as the components are more tightly coupled, but there's a risk of unintended consequences due to dependencies.
    - Microservices Architecture: Better maintainability as services are loosely coupled, allowing for independent development, deployment, and updates without affecting other parts of the system. However, managing a larger number of services can increase operational overhead.
4. **Performance:**
    - Layered Architecture: Offers better performance for monolithic applications with low network overhead and direct method calls between components.
    - Microservices Architecture: Introduces network communication overhead between services, which can impact performance, especially in latency-sensitive applications. However, it allows for better optimization of individual services and can lead to improved overall system performance through efficient scaling and resource allocation.

---

### Assumptions:

1. In our project we have created 4 different types of casinos as described below:
    
    Casino A contains: Game table A, C
    
    Casino B contains: Game table A, B
    
    Casino C contains: Game table C, D
    
    Casino D contains: Game table B, D
    
2. We have created 4 types of game tables as described below:
    
    Game table A has: Probability: 0.3, Type: Dice
    
    Game table B has: Probability: 0.7, Type: Card
    
    Game table C has: Probability: 0.5, Type: Card
    
    Game table D has: Probability: 0.5, Type: Dice
    

More different kinds of Game tables and Casinos can be created accordingly.

1. The user is supposed to Exit casino while moving out of the casino so that he can cash out the money and get it back.

### Our Github Repo link:

[https://github.com/rayaankhan/Project-3-SE](https://github.com/rayaankhan/Project-3-SE)

The `yatharth` branch contains the code for Layered Architectural Pattern
The `microservice` branch has the code for Microservice Architectural Pattern


### To run the code

* Frontend
  ```
  cd frontend  
  npm i
  npm start
  ```
* Backend (Windows)
  ```
  cd backend
  python -m flask run
  ```
  (Linux)
  ```
  cd backend
  flask run
  ```
