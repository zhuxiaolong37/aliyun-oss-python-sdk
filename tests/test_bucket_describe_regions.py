from .common import *

class TestDescribeRegions(OssTestCase):
    def test_bucket_style_normal(self):

        service = oss2.Service(oss2.Auth(OSS_ID, OSS_SECRET), OSS_ENDPOINT)
        result = service.get_describe_regions()
        self.assertEqual(200, result.status)

        exist_region = False
        for r in result.regions:
            if 'oss-cn-chengdu' == r.region:
                exist_region = True
        self.assertTrue(exist_region)

        exist_region = False
        result = service.get_describe_regions('oss-cn-chengdu')
        self.assertEqual(200, result.status)
        for r in result.regions:
            if 'oss-cn-chengdu' == r.region:
                exist_region = True

        self.assertTrue(exist_region)

    def test_bucket_style_exception(self):
        try:
            service = oss2.Service(oss2.Auth(OSS_ID, OSS_SECRET), OSS_ENDPOINT)
            service.get_describe_regions('aaa')
        except oss2.exceptions.ServerError as e:
            self.assertEqual(e.code, 'NoSuchRegion')


if __name__ == '__main__':
    unittest.main()
