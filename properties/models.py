from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
    ('house', 'House'),
    ('hotel', 'Hotel'),
    ('apartment', 'Apartment'),
    ('restaurant', 'Restaurant'),
    ('beach_land', 'Beach Land'),
    ('office', 'Office'),
    ('resort', 'Resort'),
    ('land', 'Land'),
    ('commercial', 'Commercial'),
    ('industrial', 'Industrial'),
    ('agricultural', 'Agricultural'),
    ('vacation_home', 'Vacation Home'),
    ('retail_space', 'Retail Space'),
    ('warehouse', 'Warehouse'),
    ('mixed_use', 'Mixed Use'),
    ('other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} ({self.property_type})"
    
    # House-specific model
class House(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="house")
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.FloatField(help_text="Size in square meters")
    has_garage = models.BooleanField(default=False)
    lot_size = models.FloatField(help_text="Size in square meters")
    
    def __str__(self):
            return f"{self.property.name} - House"
        
 # Apartment-specific model
class Apartment(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="apartment")
    floor_level = models.IntegerField()
    num_bedrooms = models.IntegerField()
    building_amenities = models.TextField() 
    has_balcony = models.BooleanField(default=False)
    has_parking_space = models.BooleanField(default=False)
    has_swimming_pool = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.property.name} - Apartment"  
    
    
# Office-specific model
class Office(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="office")
    num_offices = models.IntegerField()
    has_meeting_room = models.BooleanField(default=False)
    has_reception_area = models.BooleanField(default=False)
    has_parking_space = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)
    has_heating = models.BooleanField(default=False)
    has_security = models.BooleanField(default=False)
    has_elevator = models.BooleanField(default=False)
    has_fire_safety = models.BooleanField(default=False)
    has_accessibility_features = models.BooleanField(default=False)
    has_kitchenette = models.BooleanField(default=False)
    has_bathrooms = models.BooleanField(default=False)
    has_storage_space = models.BooleanField(default=False)
    has_conference_facility = models.BooleanField(default=False)
    has_break_room = models.BooleanField(default=False)
    has_telecommunication_infrastructure = models.BooleanField(default=False)
    has_parking_lot = models.BooleanField(default=False)
    has_green_certification = models.BooleanField(default=False)
    has_smart_building_technology = models.BooleanField(default=False)
    has_sustainability_features = models.BooleanField(default=False)
    has_energy_efficiency_certification = models.BooleanField(default=False)
    has_emergency_power_supply = models.BooleanField(default=False)
    has_fire_alarm_system = models.BooleanField(default=False)
    has_access_control = models.BooleanField(default=False)
    has_video_surveillance = models.BooleanField(default=False)
    has_24_hour_security = models.BooleanField(default=False)
    has_on_site_management = models.BooleanField(default=False)
    has_maintenance_services = models.BooleanField(default=False)
    has_cleaning_services = models.BooleanField(default=False)
    has_landscaping_services = models.BooleanField(default=False)
    has_waste_management_services = models.BooleanField(default=False)
    has_parking_management_services = models.BooleanField(default=False)
    has_security_patrols = models.BooleanField(default=False)
    has_access_control_system = models.BooleanField(default=False)
    has_emergency_exits = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.property.name} - Office"
    
# Hotel-specific model
class Hotel(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="hotel")
    num_rooms = models.IntegerField()
    star_rating = models.FloatField()
    has_conference_facility = models.BooleanField(default=False)
    has_swimming_pool = models.BooleanField(default=False)
    has_restaurant = models.BooleanField(default=False)
    has_gym = models.BooleanField(default=False)
    has_spa = models.BooleanField(default=False)
    has_parking_space = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)
    has_heating = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.property.name} - Hotel"
    
# Resort-specific model
class Resort(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="resort")
    num_villas = models.IntegerField()
    has_spa = models.BooleanField(default=False)
    has_gym = models.BooleanField(default=False)
    has_beach_access = models.BooleanField(default=False)
    has_water_sports = models.BooleanField(default=False)
    has_restaurant = models.BooleanField(default=False)
    has_conference_facility = models.BooleanField(default=False)
    has_swimming_pool = models.BooleanField(default=False)
    has_parking_space = models.BooleanField(default=False)
    has_security = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)
    has_heating = models.BooleanField(default=False)
    has_laundry_service = models.BooleanField(default=False)
    has_room_service = models.BooleanField(default=False)
    has_golf_course = models.BooleanField(default=False)
    has_tennis_court = models.BooleanField(default=False)
    has_basketball_court = models.BooleanField(default=False)
    has_beach_bar = models.BooleanField(default=False)
    has_kids_club = models.BooleanField(default=False)
    has_casino = models.BooleanField(default=False)
    has_night_club = models.BooleanField(default=False)
    has_shuttle_service = models.BooleanField(default=False)
    has_airport_transfer = models.BooleanField(default=False)
    has_pet_friendly = models.BooleanField(default=False)
    has_smoking_area = models.BooleanField(default=False)
    has_wheelchair_accessible = models.BooleanField(default=False)
    has_bicycle_rental = models.BooleanField(default=False)
    has_car_rental = models.BooleanField(default=False)
    has_diving_center = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.property.name} - Resort"
    
 # Restaurant-specific model
class Restaurant(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="restaurant")
    cuisine_type = models.CharField(max_length=100, help_text="Type of cuisine served")
    seating_capacity = models.IntegerField()
    kitchen_size = models.CharField(max_length=100)
    liquor_license = models.BooleanField(default=False)
    has_outdoor_seating = models.BooleanField(default=False)
    has_parking_space = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)
    has_heating = models.BooleanField(default=False)
    has_security = models.BooleanField(default=False)
    has_fire_safety = models.BooleanField(default=False)
    has_accessibility_features = models.BooleanField(default=False)
    has_kitchen_equipment = models.TextField()
    has_restaurant_licenses = models.TextField()
    has_restaurant_furniture = models.TextField()
    has_restaurant_decor = models.TextField()
    has_restaurant_signage = models.TextField()
    has_restaurant_menu = models.TextField()
    has_restaurant_suppliers = models.TextField()
    has_restaurant_staff = models.TextField()
    has_restaurant_marketing = models.TextField()
    has_restaurant_website = models.TextField()
    has_restaurant_social_media = models.TextField()
    has_restaurant_delivery = models.TextField()
    has_restaurant_takeout = models.TextField()
    has_restaurant_catering = models.TextField()
    has_restaurant_events = models.TextField()
    has_restaurant_reservations = models.TextField()
    has_restaurant_payment_processing = models.TextField()
    has_restaurant_inventory_management = models.TextField()
    has_restaurant_customer_relationship_management = models.TextField()
    
    
    def __str__(self):
        return f"{self.property.name} - Restaurant" 
    

    
# BeachLand-specific model
class BeachLand(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="beach_land")
    total_area = models.FloatField()
    beachfront_length = models.FloatField()
    zoning_type = models.CharField(max_length=100)  
    has_access_road = models.BooleanField(default=False)
    has_electricity = models.BooleanField(default=False)
    has_water_supply = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.property.title} - Beach Land"
    
# Land-specific model
class Land(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size_in_hectares = models.FloatField()
    

    def __str__(self):
        return f"{self.name} ({self.location})"

# Tenant-specific model
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=100, blank=True, null=True)
    verification_code_expiry = models.DateTimeField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lease_terms = models.TextField()
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField(max_length=20, choices=[
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annually', 'Annually'),
    ])
    payment_method = models.CharField(max_length=100, choices=[
        ('cash', 'Cash'),
        ('mpesa', 'M-Pesa'),
        ('bank_transfer', 'Bank Transfer'),
    ])
    is_signed = models.BooleanField(default=False)
    signed_date = models.DateTimeField(blank=True, null=True)
    lease_document = models.FileField(upload_to='lease_documents/', blank=True, null=True)
    is_renewed = models.BooleanField(default=False)
    renewal_date = models.DateTimeField(blank=True, null=True)
    renewal_terms = models.TextField(blank=True, null=True)
    renewal_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    renewal_fee_paid = models.BooleanField(default=False)
    renewal_fee_paid_date = models.DateTimeField(blank=True, null=True)
    is_terminated = models.BooleanField(default=False)
    termination_date = models.DateTimeField(blank=True, null=True)
    termination_reason = models.TextField(blank=True, null=True)
    termination_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    termination_fee_paid = models.BooleanField(default=False)
    termination_fee_paid_date = models.DateTimeField(blank=True, null=True)
    is_terminated_by_tenant = models.BooleanField(default=False)
    is_terminated_by_landlord = models.BooleanField(default=False)
    termination_notice_period = models.IntegerField(default=30, help_text="Notice period in days")
    is_rent_paid = models.BooleanField(default=False)
    rent_payment_date = models.DateTimeField(blank=True, null=True)
    rent_payment_receipt = models.FileField(upload_to='rent_payment_receipts/', blank=True, null=True)
    rent_payment_method = models.CharField(max_length=100, choices=[
        ('cash', 'Cash'),
        ('mpesa', 'M-Pesa'),
        ('bank_transfer', 'Bank Transfer'),
    ])
    rent_payment_reference_number = models.CharField(max_length=50, blank=True, null=True)
    rent_payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending')
    

    def __str__(self):
        return f"{self.tenant.name} - {self.property.name}"
    
class RentPayment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100, choices=[
        ('cash', 'Cash'),
        ('mpesa', 'M-Pesa'),
        ('bank_transfer', 'Bank Transfer'),
    ])
    receipt_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Payment by {self.tenant.name} - {self.amount_paid}"

# Commercial-specific model
class Commercial(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="commercial")
    total_area = models.FloatField()
    zoning_type = models.CharField(max_length=100)
    has_parking_space = models.BooleanField(default=False)
    has_security = models.BooleanField(default=False)
    has_electricity = models.BooleanField(default=False)
    has_water_supply = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name} - Commercial"

# Industrial-specific model
class Industrial(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="industrial")
    industrial_type = models.CharField(max_length=100, help_text="Type of industrial property")
    square_footage = models.FloatField(help_text="Total area in square meters")
    
    
    def __str__(self):
        return f"{self.property.name} - Industrial" 
    
# Agricultural-specific model
class Agricultural(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="agricultural")
    total_area = models.FloatField()
    crop_type = models.CharField(max_length=100)
    has_irrigation_system = models.BooleanField(default=False)
    has_fencing = models.BooleanField(default=False)
    has_access_road = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name} - Agricultural"

# Vacation-specific model
class Vacation(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="vacation_home")
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    has_swimming_pool = models.BooleanField(default=False)
    has_gym = models.BooleanField(default=False)
    has_parking_space = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    has_air_conditioning = models.BooleanField(default=False)
    has_heating = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name} - Vacation"
    
# Retail-specific model

class Retail(models.Model):
    name = models.CharField(max_length=255)
    square_footage = models.FloatField(help_text="Total area in square feet")
    retail_type = models.CharField(max_length=50, choices=[('store', 'Store'), ('shop', 'Shop')])  # This field defines the retail type
    location = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.property.name} - Retail"
    
# Warehouse-specific model
class Warehouse(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="warehouse")
    total_area = models.FloatField()
    has_loading_dock = models.BooleanField(default=False)
    has_security = models.BooleanField(default=False)
    has_electricity = models.BooleanField(default=False)
    has_water_supply = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name} - Warehouse"
    
# MixedUse-specific model
class MixedUse(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="mixed_use")
    property_type = models.CharField(max_length=20)
    description = models.TextField()
    has_parking_space = models.BooleanField(default=False)
    has_security = models.BooleanField(default=False)
    has_electricity = models.BooleanField(default=False)
    has_water_supply = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name} - Mixed Use"
    
# Other-specific model
class Other(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name="other")
    description = models.TextField()
    has_parking_space = models.BooleanField(default=False)
    has_security = models.BooleanField(default=False)
    has_electricity = models.BooleanField(default=False)
    has_water_supply = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name} - Other"
    
    