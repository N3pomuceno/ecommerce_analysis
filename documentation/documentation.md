# sql_project

This project is to enhance my SQL skills, mostly DML, where I can use to make analysis and show more insights from a especific database.

The [database](https://www.kaggle.com/datasets/imranalishahh/comprehensive-synthetic-e-commerce-dataset) is from Kaggle, it is a synthetic e-commerce dataset, and probrably a good way to enhance my SQL skills. Like the introduction of the dataset page:

### Dataset Description

This dataset is a synthetic e-commerce dataset designed to provide a comprehensive view of transaction, customer, product, and advertising data in a dynamic marketplace. It simulates real-world scenarios with seasonal effects, regional variations, advertising metrics, and customer purchasing behaviors. This dataset can serve as a valuable resource for exploring e-commerce analytics, customer segmentation, product performance, and marketing effectiveness.

The dataset includes detailed transaction-level data featuring product categories, customer demographics, discounts, revenue, and advertising metrics such as impressions, clicks, conversion rates, and ad spend. Seasonal trends and regional multipliers are integrated into the data to create realistic patterns that mimic consumer behavior across different times of the year and geographic regions.

Potential Analyses
1. Customer Insights

* Perform customer segmentation based on demographics, lifetime value, and purchase behavior.
* Analyze trends in customer behavior across regions or product categories.

2. Product Performance

* Identify top-performing products by revenue or units sold.
* Evaluate the impact of discounts and promotions on product sales.

3. Marketing Analytics

* Measure the effectiveness of advertising using CTR, CPC, and conversion rates.
* Assess how ad spend correlates with revenue and impressions.

4. Seasonal Trends

* Analyze seasonality effects on sales volume and revenue.
* Explore spikes in revenue or sales during holiday periods.

5. Regional Analysis

* Investigate regional performance trends using the regional multipliers.
* Examine customer preferences across different regions.

6. Data Science Applications

* Build predictive models for sales forecasting.
* Create clustering models for customer segmentation or product categorization.
* Develop optimization strategies for advertising spend or inventory management.

---

### About the Dataset: Column Descriptions

This dataset provides detailed synthetic data representing transactions, customer demographics, product information, and advertising metrics in an e-commerce setting. Below is an explanation of each column in the dataset:
Transaction Data

    Transaction_ID: Unique identifier for each transaction.
    Customer_ID: Unique identifier for the customer associated with the transaction.
    Product_ID: Unique identifier for the product purchased in the transaction.
    Transaction_Date: The date when the transaction occurred.

Product Information

    Category: The category to which the product belongs (e.g., Electronics, Clothing).
    Units_Sold: The quantity of the product sold in the transaction.
    Discount_Applied: The discount percentage applied to the product during the transaction.
    Revenue: Total revenue generated from the transaction, calculated as Price x Units Sold x (1 - Discount).

Customer Demographics

    Customer_ID: Unique identifier for each customer (repeated for easier reference).
    Age: Age of the customer.
    Gender: Gender of the customer (Male, Female, Other).
    Location: Geographical location of the customer.
    Customer_Lifetime_Value: Estimated lifetime value of the customer to the e-commerce platform.

Advertising Metrics

    Clicks: Number of ad clicks associated with the product during the time of the transaction.
    Impressions: Number of ad impressions served during the campaign.
    Conversion_Rate: Calculated as Clicks / Impressions, representing the percentage of impressions that resulted in clicks.
    Ad_CTR: Click-through rate (CTR) for the advertisement, representing the effectiveness of the ad campaign.
    Ad_CPC: Cost-per-click for the advertisement.
    Ad_Spend: Total advertising spend for the product, calculated as Ad_CTR x Ad_CPC x 1000.

Seasonal and Regional Information

    Region: The geographical region where the transaction occurred (e.g., North America, Europe, Asia).
    Seasonality Effects: Implied through patterns in transaction dates and revenue, reflecting holiday promotions and season-based purchasing trends.

This dataset combines detailed attributes from multiple domains, allowing for in-depth analyses of customer behavior, product performance, marketing effectiveness, and seasonal trends.




So, within these potential analysis, I'll make a series of questions that can be answered throught SQL.



---

In the end what I want is to have the capability to do DML commands through some software like dbeaver or tablePlus, or with python, executing with command line.

In this project I'll force the dbt tool, so the python file `dbt_init.py` is a second plan if all dbt plan goes to nothing. So the plan is to create a dbt project and all the sql will be there. 
