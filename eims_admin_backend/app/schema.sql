-- Create supplier_social_media table
CREATE TABLE IF NOT EXISTS supplier_social_media (
    social_media_id INTEGER NOT NULL DEFAULT nextval('supplier_social_media_social_media_id_seq'::regclass),
    supplier_id INTEGER NOT NULL,
    platform VARCHAR(100) NOT NULL,
    handle VARCHAR(255) NOT NULL,
    url VARCHAR(255),
    CONSTRAINT supplier_social_media_pkey PRIMARY KEY (social_media_id),
    CONSTRAINT supplier_social_media_supplier_id_fkey FOREIGN KEY (supplier_id)
        REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);

    -- Table for storing event package configurations
CREATE TABLE IF NOT EXISTS event_package_configurations (
    config_id SERIAL PRIMARY KEY,
    events_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (events_id) REFERENCES events(events_id),
    FOREIGN KEY (package_id) REFERENCES event_packages(package_id)
);

-- Table for storing configured suppliers from the package
CREATE TABLE IF NOT EXISTS event_package_suppliers (
    id SERIAL PRIMARY KEY,
    config_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    original_price DECIMAL(10,2),
    modified_price DECIMAL(10,2),
    is_modified BOOLEAN DEFAULT false,
    is_removed BOOLEAN DEFAULT false,
    remarks TEXT,
    FOREIGN KEY (config_id) REFERENCES event_package_configurations(config_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Table for storing configured services from the package
DROP TABLE IF EXISTS event_package_services CASCADE;
CREATE TABLE IF NOT EXISTS event_package_services (
    event_package_service_id SERIAL PRIMARY KEY,
    package_id INTEGER NOT NULL,
    package_service_id INTEGER NOT NULL,
    CONSTRAINT idx_event_package_services UNIQUE (package_id, package_service_id),
    CONSTRAINT fk_event_package FOREIGN KEY (package_id) 
        REFERENCES event_packages(package_id) ON DELETE CASCADE,
    CONSTRAINT fk_package_service FOREIGN KEY (package_service_id) 
        REFERENCES package_service(package_service_id) ON DELETE CASCADE
);

-- Table for storing configured outfits from the package
CREATE TABLE IF NOT EXISTS event_package_outfits (
    id SERIAL PRIMARY KEY,
    config_id INTEGER NOT NULL,
    outfit_id INTEGER,
    gown_package_id INTEGER,
    original_price DECIMAL(10,2),
    modified_price DECIMAL(10,2),
    is_modified BOOLEAN DEFAULT false,
    is_removed BOOLEAN DEFAULT false,
    remarks TEXT,
    FOREIGN KEY (config_id) REFERENCES event_package_configurations(config_id),
    FOREIGN KEY (outfit_id) REFERENCES outfits(outfit_id),
    FOREIGN KEY (gown_package_id) REFERENCES gown_packages(gown_package_id)
);

-- Table for storing additional (non-package) items
CREATE TABLE IF NOT EXISTS event_additional_items (
    id SERIAL PRIMARY KEY,
    events_id INTEGER NOT NULL,
    item_type VARCHAR(50) NOT NULL, -- 'supplier', 'service', 'outfit'
    item_id INTEGER NOT NULL,
    price DECIMAL(10,2),
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (events_id) REFERENCES events(events_id)
);
