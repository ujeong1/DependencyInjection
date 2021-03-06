from injector import inject
from MyDatabase import DatabaseBase

class facebook_ads_tracker_service:
    @inject
    def __init__(self, connection: DatabaseBase):
        self.table_name_facebook_ads = "FB_ads_table"
        self.table_name_facebook_job = "job_table"
        self.connection = connection
        print(f"DatabaseBase instance is {connection}")

    def get_data(self):
        db = self.connection.getDB()
        cursor = db[self.table_name_facebook_ads]
        data = cursor.find()
        for x in data:
            print(x)
        return data

    def set_data(self, instance):
        db = self.connection.getDB()
        cursor = db[self.table_name_facebook_job]
        if instance == None:
            #just give an instance as defined. 
            instance = self.query_construct()
        cursor.insert_one(instance)
        return "An instance has been inserted in Facebook Ads DB."

    def delete_data(self):
        db = self.connection.getDB()
        cursor = db[self.table_name_facebook_ads]
        cursor.drop()
        cursor = db[self.table_name_facebook_job]
        cursor.drop()
        return "successfully deleted"
        
    def query_construct(self):
        query = dict()
        query["access_token"] = "SOME TOKEN HERE"
        query["action"] = "search"
        query["fields"] = "ad_creative_body, ad_snapshot_url, ad_creation_time, ad_creative_link_title," \
                          "ad_creative_link_description, ad_creative_link_caption, " \
                          "ad_delivery_start_time, ad_delivery_stop_time, impressions, currency, demographic_distribution," \
                          "funding_entity, page_name, page_id, potential_reach, region_distribution, spend"
        query["after_date"] = ""
        query["batch_size"] = 16
        query["retry_limit"] = 3
        query["verbose"] = False
        # query["search_page_ids"] = ""
        query["search_term"] = "test"
        query["country"] = ["BR", "GB", "US"]
        query["ad_active_status"] = "ALL"
        query["ad_category"] = "ALL"  # CREDIT_ADS, EMPLOYMENT_ADS, HOUSING_ADS, POLITICAL_AND_ISSUE_ADS, UNCATEGORIZED_ADS
        query["publisher_platforms"] = "FACEBOOK"  # INSTAGRAM, AUDIENCE_NETWORK, MESSENGER, WHATSAPP
        return query
