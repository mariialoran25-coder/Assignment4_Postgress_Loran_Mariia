CREATE view hms.active_booking_report AS
SELECT b.IDBooking  ,g.first_name, g.last_name, r.room_number, b.arrival_date
FROM hms.Booking b
JOIN hms.Guests g ON b.IDGuest = g.IDGuest
JOIN hms.Room r ON b.IDRoom = r.IDRoom;

