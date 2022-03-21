import os

from django.conf import settings
from django.db import models

from accounts.models import User
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.size
    limit_mb = 3
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("이미지의 최대 크기는 %s MB 입니다." % limit_mb)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 잃어버렸어요 게시판
class LostPetBoard(TimestampedModel):
    lost_board_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()

    lost_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-lost_board_no']


# 잃어버렸어요 게시판 이미지
class LostPetBoardImage(models.Model):
    lost_image_no = models.AutoField(primary_key=True)

    image = models.ImageField(blank=False, validators=[validate_image])

    lost_board_no = models.ForeignKey(LostPetBoard, on_delete=models.CASCADE, related_name="board_image")

    class Meta:
        ordering = ['-lost_image_no']

    def save(self, *args, **kwargs):
        self.lost_board_no, created = LostPetBoard.objects.get_or_create(
            
        )
        print(self)
        print(self.board_image)

        board_image_save = self.board_image
        super(LostPetBoard, self).save(*args, **kwargs)
        new_image = LostPetBoardImage(image=board_image_save, lost_board_no_id=self)
        new_image.save()