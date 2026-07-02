----------------------------------------------------------------------
CREATE USER h_admin WITH Password 'qwerty123';
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA hms TO h_admin;

CREATE USER h_staff WITH Password 'qwerty_staff_123';
GRANT SELECT, INSERT, UPDATE ON  hms.Booking TO h_staff;

CREATE USER h_auditor WITH Password 'read_only123';
GRANT USAGE ON SCHEMA hms TO h_auditor;
GRANT SELECT ON ALL TABLES IN SCHEMA hms TO h_auditor;
----------------------------------------------------------------------
