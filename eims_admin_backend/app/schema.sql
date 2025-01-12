-- Create supplier_social_media table
CREATE TABLE IF NOT EXISTS supplier_social_media (
    social_media_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT NOT NULL,
    platform VARCHAR(50) NOT NULL,
    handle VARCHAR(100) NOT NULL,
    url VARCHAR(255),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);
