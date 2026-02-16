import shutil

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import RequestFactory

from showroom.views import ShowroomView


class Command(BaseCommand):
    help = "Build the showroom as a static site"

    def handle(self, *args, **options):
        build_dir = settings.BUILD_DIR
        if build_dir.exists():
            shutil.rmtree(build_dir)
        build_dir.mkdir()

        # Copy static files
        static_dir = build_dir / "static"
        shutil.copytree(settings.BASE_DIR / "static", static_dir)

        # Render the view
        request = RequestFactory().get("/")
        response = ShowroomView.as_view()(request)
        response.render()
        (build_dir / "index.html").write_text(response.content.decode())

        self.stdout.write(self.style.SUCCESS(f"Built to {build_dir}"))
