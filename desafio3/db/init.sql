CREATE TABLE IF NOT EXISTS items (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT
);

INSERT INTO items (name, description) VALUES
  ('Banana', 'Fruta amarela, rica em potássio'),
  ('Maçã', 'Fruta crocante e doce'),
  ('Laranja', 'Fruta cítrica, ótima para suco')
ON CONFLICT DO NOTHING;
