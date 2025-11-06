DROP TABLE IF EXISTS `employees`;

CREATE TABLE `employees` (
  `first_name`   VARCHAR(255) NOT NULL COMMENT 'The first name of the employee',
  `last_name`    VARCHAR(255) NOT NULL COMMENT 'The last name of the employee',
  `seniority`    INT          NOT NULL COMMENT 'Number of years of seniority within the organization',
  PRIMARY KEY (`first_name`, `last_name`)
) ENGINE=InnoDB;


INSERT INTO `employees` (`first_name`, `last_name`, `seniority`) VALUES
  ('Marie',   'Dubois',          4),   -- zaal, Franstalig personeel komt vaak voor
  ('Bram',    'Peeters',         6),   -- sous-chef
  ('Sofie',   'De Smet',         3),   -- zaal
  ('Jean',    'Lambert',        12),   -- chef-kok, jaren ervaring
  ('Anouk',   'Vermeulen',       1),   -- bar/trainee
  ('Youssef', 'El Amrani',       2),   -- commis
  ('Chantal', 'Lefebvre',        8),   -- maître d’hôtel
  ('Koen',    'Van den Bossche',10),   -- sommelier
  ('Leïla',   'Benchekroun',     5),   -- patissier
  ('Dries',   'Maes',            7);