-- Add status column to the wishlist_suppliers table if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'wishlist_suppliers' AND column_name = 'status'
    ) THEN
        ALTER TABLE wishlist_suppliers ADD COLUMN status VARCHAR(20) DEFAULT 'Pending';
    END IF;
END
$$;

-- Add status column to the wishlist_outfits table if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_name = 'wishlist_outfits' AND column_name = 'status'
    ) THEN
        ALTER TABLE wishlist_outfits ADD COLUMN status VARCHAR(20) DEFAULT 'Pending';
    END IF;
END
$$; 