//Light.h
#ifndef LIGHT_H
#define LIGHT_H


class Light
{
    public:
        Light();
        virtual ~Light();

        Status onLight();
        Status offLight();

    protected:

    private:
};

#endif // LIGHT_H
