
SELECT u.nom_usuario, u.email, u.contraseña, r.descripcion
from Usuario as u INNER JOIN Rol as r ON u.id_rol = r.id_rol
where (u.nom_usuario = 'Luis' or u.email = 'Luis') and u.contraseña = '123';