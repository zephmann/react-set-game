from high_scores.models import HighScore
from high_scores.serializers import HighScoreSerializer
from rest_framework import viewsets


class HighScoreListCreate(viewsets.ModelViewSet):
    queryset = HighScore.objects.all()
    serializer_class = HighScoreSerializer
