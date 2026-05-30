-- Скрипт инициализации базы данных OSINT Scanner

-- 1. Создаем таблицу сайтов
CREATE TABLE IF NOT EXISTS sites (
    id SERIAL PRIMARY KEY,
    domain VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Индекс для быстрого поиска по домену
CREATE INDEX IF NOT EXISTS ix_sites_domain ON sites (domain);
CREATE INDEX IF NOT EXISTS ix_sites_id ON sites (id);

-- 2. Создаем таблицу сканов
CREATE TABLE IF NOT EXISTS scans (
    id SERIAL PRIMARY KEY,
    site_id INTEGER NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    raw_data JSONB, -- Используем JSONB для эффективного хранения в Postgres
    ai_report TEXT,
    
    -- Внешний ключ: при удалении сайта удаляются все его сканы (cascade)
    CONSTRAINT fk_site
        FOREIGN KEY(site_id) 
        REFERENCES sites(id) 
        ON DELETE CASCADE
);

-- Индекс для внешнего ключа и поиска
CREATE INDEX IF NOT EXISTS ix_scans_id ON scans (id);
CREATE INDEX IF NOT EXISTS ix_scans_site_id ON scans (site_id);
