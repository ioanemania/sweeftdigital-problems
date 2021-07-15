/* გვაქვს teacher ცხრილი, რომელსაც აქვს შემდეგი მახასიათებლები:
 სახელი, გვარი, სქესი, საგანი. გვაქვს pupil ცხრილი, რომელსაც აქვს შემდეგი
მახასიათებლები: სახელი, გვარი, სქესი, კლასი. ააგეთ ნებისმიერ რელაციურ ბაზაში
ისეთი დამოკიდებულება, რომელიც საშუალებას მოგვცემს, რომ მასწავლებელმა ასწავლოს
რამოდენიმე მოსწავლეს და ამავდროულად მოსწავლეს ჰყავდეს რამდენიმე მასწავლებელი
(როგორც რეალურ ცხოვრებაში). */

/* 1. დაწერეთ SQL რომელიც ააგებს შესაბამის table-ებს. */

/* დაწერილია mysql ბაზაზე. */ 
set NAMES utf8;

CREATE TABLE IF NOT EXISTS teacher (
  id     INT  AUTO_INCREMENT PRIMARY KEY,
  სახელი TEXT NOT NULL,
  გვარი  TEXT NOT NULL,
  სქესი  TEXT NOT NULL,
  საგანი TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pupil (
  id     INT  AUTO_INCREMENT PRIMARY KEY,
  სახელი TEXT NOT NULL,
  გვარი  TEXT NOT NULL,
  სქესი  TEXT NOT NULL,
  კლასი  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS teacher_pupil (
  id INT AUTO_INCREMENT PRIMARY KEY,
  teacher_id INT,
  pupil_id INT,
  FOREIGN KEY (teacher_id) REFERENCES teacher(id),
  FOREIGN KEY (pupil_id) REFERENCES pupil(id)
);

/* 2. დაწერეთ SQL რომელიც დააბრუნებს ყველა მასწავლებელს, რომელიც ასწავლის
 * მოსწავლეს, რომელის სახელია: “გიორგი”. */

/* დასატესტად ცხრილებს ხელით შევავსებ. */
DELETE FROM teacher_pupil;
DELETE FROM teacher;
DELETE FROM pupil;

INSERT INTO teacher
VALUES 
(1, "საბა", "ხუციშვილი", "მამრობითი", "მათემატიკა"),
(2, "ზურაბ", "აბულაძე", "მამრობითი", "ისტორია"),
(3, "ირაკლი", "მიქელაძე", "მამრობითი", "გეოგრაფია"),
(4, "ნიკოლოზ", "ბაირამოვი", "მამრობითი", "ინგლისური ენა"),
(5, "ლუკა", "შენგელია", "მამრობითი", "ბიოლოგია"),
(6, "ალექსანდრე", "ტაბატაძე", "მამრობითი", "ფიზიკა");

INSERT INTO pupil
VALUES
(1, "ნინო", "დიასამიძე", "მდედრობითი", "10ა"),
(2, "გიორგი", "აბაშიძე", "მამრობითი", "10ა"),
(3, "გიორგი", "ბერიძე", "მამრობითი", "10ა"),
(4, "ნიკოლოზი", "მამედოვი", "მამრობითი", "9ბ"),
(5, "ანანო", "კაპანაძე", "მდედრობითი", "9ბ"),
(6, "მიხეილ", "ალიევი", "მამრობითი", "11ე"),
(7, "მარიამ", "გელაშვილი", "მდედრობითი", "9ბ"),
(8, "გიორგი", "მაისურაძე", "მამრობითი", "11ე"),
(9, "ლაშა", "წიკლაური", "მამრობითი", "9ბ");

/* მასწავლებლებსა და მოსწავლეებს შორის კავშირი. */
INSERT INTO teacher_pupil (teacher_id, pupil_id)
VALUES
(1, 3),
(2, 8),
(3, 1),
(4, 6),
(5, 5),
(6, 4),
(6, 7),
(6, 2),
(6, 9);

SELECT teacher.*
FROM pupil
JOIN teacher_pupil
ON pupil.id = teacher_pupil.pupil_id
JOIN teacher
ON teacher_pupil.teacher_id = teacher.id
WHERE pupil.სახელი="გიორგი";
