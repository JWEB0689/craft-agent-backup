# Shopify Source Guide

This guide will walk you through configuring the Shopify source to connect to your store.

## Configuration

You will need to configure your **Store Name** and **Access Token** to use this source.

### 1. Find Your Store Name

Your store name is the part of your Shopify URL before `.myshopify.com`. For example, if your Shopify admin URL is `my-awesome-store.myshopify.com/admin`, your store name is `my-awesome-store`.

### 2. Generate an Admin API Access Token

To get your Admin API access token, you need to create a custom app in your Shopify admin dashboard.

1.  Log in to your Shopify admin dashboard.
2.  In the left-hand menu, go to **Apps**.
3.  Click on **Develop apps for your store**. If this option is not visible, you may need to enable app development in the settings.
4.  Click **Create an app**.
5.  Provide a name for your app (e.g., "Craft Agent Integration") and select an app developer.
6.  Click **Create app**.
7.  Once the app is created, navigate to the **API credentials** tab.
8.  Under the **Admin API access** section, click **Configure Admin API scopes**.
9.  Select the permissions (scopes) that you want to grant to the app. For full functionality, you may want to grant access to products, orders, and customers.
10. Click **Save**.
11. Click the **Install app** button at the top right of the page.
12. A confirmation dialog will appear. Click **Install** to proceed.
13. After installation, the **Admin API access token** will be revealed. Copy this token.

### 3. Configure the Source

1.  In Craft Agent, go to the sources page and find the Shopify source.
2.  Click **Configure**.
3.  You will be prompted to enter your `store_name` and the `Admin API access token` you just copied.
4.  Save the configuration.

You are now ready to use the Shopify source!
