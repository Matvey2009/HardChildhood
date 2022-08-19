/*SQlite3*/
	--Команды транслятора
	--.open lesson.db
--Создание таблицы
CREATE TABLE `user`(
	`name` TEXT,
	`age` INTEGER
);

--Добавляем данные
INSERT INTO `user` VALUES(
	'matvey', 48
);

--Получение данных
SELECT * FROM `user`;